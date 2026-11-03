// Which language the window speaks, and the words for it.
//
// English is the source: every string in this program is written in English
// and looked up here by that same text. A string with no translation is shown
// as it was written, so a missing entry is a word in English and never a blank
// or a key. The engine is told the same choice through HFAC_LANG, so the
// questions it asks come back in the language the window is in.
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Runtime.InteropServices;
using Avalonia.Controls;
using Avalonia.LogicalTree;

namespace Shell.Engine;

public static partial class L
{
    /// <summary>"pt" or "en". HFAC_LANG decides first, then the system's own setting.</summary>
    public static readonly string Code = Detect();

    // a property, not a field: Pt is declared in another file, and the order
    // static fields of a partial class are set in across files is not defined
    static Dictionary<string, string>? Map => Code == "pt" ? Pt : null;

    /// <summary>The translation of an English string, or the string itself.</summary>
    public static string T(string english) =>
        Map is not null && Map.TryGetValue(english, out var said) ? said : english;

    /// <summary>A translated format string, filled in. {0}, {1}… as string.Format.</summary>
    public static string F(string english, params object?[] args) =>
        string.Format(T(english), args);

    /// <summary>Translate the text a view was declared with.
    ///
    /// Called once, right after InitializeComponent, so it only ever sees what
    /// the XAML wrote. Text set later by code goes through T() itself.</summary>
    public static void Apply(Control root)
    {
        if (Map is null) return;
        foreach (var c in new[] { root }.Concat(root.GetLogicalDescendants().OfType<Control>()))
        {
            switch (c)
            {
                case Window w when w.Title is { } title:
                    w.Title = T(title);
                    break;
                case TextBlock tb when tb.Text is { } text:
                    tb.Text = T(text);
                    break;
                case TextBox box when box.Watermark is { } mark:
                    box.Watermark = T(mark);
                    break;
                case ContentControl cc when cc.Content is string content:
                    cc.Content = T(content);
                    break;
            }
        }
    }

    static string Detect()
    {
        var chosen = Environment.GetEnvironmentVariable("HFAC_LANG");
        var code = Normalise(chosen) ?? Normalise(SystemLanguage()) ?? "en";
        // the engine runs as a child of this window and reads the same variable
        Environment.SetEnvironmentVariable("HFAC_LANG", code);
        return code;
    }

    static string? Normalise(string? said)
    {
        if (string.IsNullOrWhiteSpace(said)) return null;
        said = said.Trim().ToLowerInvariant();
        if (said.StartsWith("pt", StringComparison.Ordinal)) return "pt";
        if (said.StartsWith("en", StringComparison.Ordinal)) return "en";
        // C and POSIX say nothing about a language, so keep looking
        return said is "c" or "posix" || said.StartsWith("c.", StringComparison.Ordinal)
            ? null : "en";
    }

    [DllImport("kernel32.dll")]
    static extern ushort GetUserDefaultUILanguage();

    /// <summary>The user's interface language as the system states it.
    ///
    /// Not CultureInfo: this program is built with InvariantGlobalization, so
    /// CultureInfo is always the invariant culture and says nothing.</summary>
    static string? SystemLanguage()
    {
        try
        {
            if (OperatingSystem.IsWindows())
                // 0x16 is the primary language id for Portuguese
                return (GetUserDefaultUILanguage() & 0x3FF) == 0x16 ? "pt" : "en";
            foreach (var name in new[] { "LC_ALL", "LC_MESSAGES", "LANG" })
                if (Normalise(Environment.GetEnvironmentVariable(name)) is { } code)
                    return code;
            if (OperatingSystem.IsMacOS())
            {
                // an app opened from Finder has no LANG, so ask the defaults
                var info = new ProcessStartInfo("defaults", "read -g AppleLanguages")
                {
                    RedirectStandardOutput = true, UseShellExecute = false,
                    CreateNoWindow = true,
                };
                using var p = Process.Start(info);
                var said = p?.StandardOutput.ReadToEnd() ?? "";
                p?.WaitForExit(3000);
                var first = said.Split('"', StringSplitOptions.RemoveEmptyEntries)
                                .Select(s => s.Trim())
                                .FirstOrDefault(s => s.Length >= 2 && char.IsLetter(s[0]));
                return first;
            }
        }
        catch
        {
            // a language that cannot be read is English, not a crash
        }
        return null;
    }
}
