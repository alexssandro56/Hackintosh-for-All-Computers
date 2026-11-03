"""The language the builder speaks, and the words for it.

English is the source. Every message in these tools is written in English, and
a translation is looked up by that same English text when it is shown, not
where it is written: what the console prints and what the protocol sends pass
through tr_line() on the way out. So the 190 places that print do not change,
a message nobody translated yet is shown in English rather than as a blank or a
key, and the selftest - which reads English - reads the same thing it always
did.

A message with a value in it is matched as a template: the English entry
'{} tables in {}' matches '12 tables in C:\\ACPI', and the two values are put
back into the translation in order, or in the order its {0}, {1} name them.
A value that is itself a known message is translated too, so 'this machine'
inside 'building for this machine' comes out in the same language as the rest.

The language comes from HFAC_LANG (pt or en) first, which is what the window
sets for the engine it starts, and then from the system's own setting.
"""
import os
import re
import subprocess
import sys

ANSI = re.compile(r'(\033\[[0-9;]*m)')


def _normalise(said):
    if not said:
        return None
    said = said.strip().lower()
    if said.startswith('pt'):
        return 'pt'
    if said.startswith('en'):
        return 'en'
    # C and POSIX say nothing about a language
    if said in ('c', 'posix') or said.startswith('c.'):
        return None
    return 'en'


def _system():
    try:
        if sys.platform == 'win32':
            import ctypes
            lang = ctypes.windll.kernel32.GetUserDefaultUILanguage()
            # 0x16 is the primary language id for Portuguese
            return 'pt' if (lang & 0x3FF) == 0x16 else 'en'
        for name in ('LC_ALL', 'LC_MESSAGES', 'LANG'):
            code = _normalise(os.environ.get(name))
            if code:
                return code
        if sys.platform == 'darwin':
            # an app started from Finder has no LANG
            said = subprocess.run(['defaults', 'read', '-g', 'AppleLanguages'],
                                  capture_output=True, text=True, timeout=3,
                                  encoding='utf-8', errors='replace').stdout
            first = re.search(r'"?([A-Za-z]{2}[-_A-Za-z]*)"?', said)
            return _normalise(first.group(1)) if first else None
    except Exception:                      # noqa: BLE001 - English, not a crash
        return None
    return None


_LANG = None


def lang():
    """'pt' or 'en', decided once."""
    global _LANG
    if _LANG is None:
        _LANG = _normalise(os.environ.get('HFAC_LANG')) or _system() or 'en'
    return _LANG


_TABLE = None
_FMT = {}
_EXACT = {}
_TEMPLATES = []


def _load():
    global _TABLE
    if _TABLE is not None:
        return
    _TABLE = {}
    global _FMT
    if lang() == 'pt':
        import lang_pt
        _TABLE = lang_pt.PT
        _FMT = lang_pt.FMT
    for english, said in _TABLE.items():
        if '{' in english:
            parts = re.split(r'\{[^{}]*\}', english)
            pattern = '(.+?)'.join(re.escape(p) for p in parts)
            _TEMPLATES.append((re.compile(f'^{pattern}$', re.S), said))
        else:
            _EXACT[english] = said
    # the most specific first: '{} of {} devices' has to be tried before a
    # shorter template that would also match it and say less
    _TEMPLATES.sort(key=lambda t: -len(re.sub(r'\(\.\+\?\)', '', t[0].pattern)))


def tr(text):
    """The translation of one message, or the message itself."""
    if not text or lang() == 'en':
        return text
    _load()
    if not _TABLE:
        return text
    lead = text[:len(text) - len(text.lstrip())]
    trail = text[len(text.rstrip()):]
    core = text.strip()
    if not core:
        return text
    said = _EXACT.get(core)
    if said is None:
        said = _template(core)
        if said is None:
            return text
    return lead + said + trail


def fmt(template, *values):
    """A message built here from a template, in the language being spoken.

    For the few that cannot be matched after they are printed, because the
    English template would match too much: '{} to {}' is one."""
    if lang() != 'en':
        _load()
        template = _FMT.get(template) or _TABLE.get(template, template)
    return template.format(*values)


def _template(core):
    for pattern, said in _TEMPLATES:
        m = pattern.match(core)
        if not m:
            continue
        # shorter than the message it came from, so this always ends
        values = [tr(v) for v in m.groups()]
        try:
            return said.format(*values)
        except (IndexError, KeyError, ValueError):
            return None
    return None


def tr_line(line):
    """One printed line, translated a run of colour at a time.

    Colour codes split a line into the same runs the window draws, and each
    run is a message or part of one, so each is looked up on its own. The
    whole line is tried first, for the ones a colour does not split."""
    if lang() == 'en' or not line:
        return line
    return ''.join(p if ANSI.fullmatch(p) else _run(p) for p in ANSI.split(line))


COLUMNS = re.compile(r'(\s{2,})')


def _run(text):
    """One run of one colour: the whole of it, or else column by column.

    Tables are lined up with runs of spaces, and with no colour to split them
    - the console writing to a pipe has none - a row is one run. Two spaces
    or more is where a column ends, so each column is then tried on its own."""
    if not COLUMNS.search(text.strip()):
        return tr(text)
    if lang() != 'en':
        _load()
    said = _EXACT.get(text.strip())
    if said is not None:
        return tr(text)
    # columns before templates: '{} items' would otherwise take the whole of
    # 'payload      39 items' as its value and leave the label in English
    split = ''.join(p if COLUMNS.fullmatch(p) else tr(p) for p in COLUMNS.split(text))
    return split if split != text else tr(text)


# Fields of the JSON documents a window draws that hold words for a person.
# Everything else in them is a key, an id, a path or a value the window
# compares against, and none of that may change with the language.
SHOWN = {'note', 'detail', 'gap', 'covers', 'area', 'why', 'network_note',
         'text', 'complaint', 'trouble', 'message', 'question', 'what',
         'from_because', 'to_because', 'gpu_note', 'source_note'}


def document(doc):
    """A JSON document with the words in it translated, in place."""
    if lang() == 'en':
        return doc
    if isinstance(doc, dict):
        for k, v in doc.items():
            if isinstance(v, str) and k in SHOWN:
                doc[k] = tr(v)
            else:
                document(v)
    elif isinstance(doc, list):
        for v in doc:
            document(v)
    return doc


class Writer:
    """sys.stdout, translated a line at a time on the way out."""

    def __init__(self, out):
        self.out = out
        self.pending = ''

    def write(self, s):
        self.pending += s
        while '\n' in self.pending:
            line, self.pending = self.pending.split('\n', 1)
            self.out.write(tr_line(line) + '\n')
        return len(s)

    def flush(self):
        if self.pending:
            self.out.write(tr_line(self.pending))
            self.pending = ''
        self.out.flush()

    def isatty(self):
        return self.out.isatty()

    def __getattr__(self, name):
        return getattr(self.out, name)
