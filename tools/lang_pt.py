"""Português do Brasil, for i18n.py.

The key is the English message as the tools print it, with each value in it
written as {}. The translation takes the values in the same order with {}, or
in its own order with {0}, {1}. A message that is not here is shown in English.

Not here on purpose: anything that is run rather than read (PowerShell, shell
lines, the script installer.py hands to a password prompt), names of products
and CPU generations, and file names.
"""

PT = {
    # ---- setup.py: the questions ------------------------------------------
    'none of these': 'nenhuma destas',
    'enter a number from the list': 'digite um número da lista',
    'OpenCore EFI builder': 'Construtor de EFI do OpenCore',
    'Which machine is this EFI for?': 'Para qual máquina é esta EFI?',
    'This machine': 'Esta máquina',
    'Another machine, and I have its hardware report': 'Outra máquina, e eu tenho o relatório de hardware dela',
    'Another machine, and I do not have one': 'Outra máquina, e eu não tenho o relatório',
    "Neither - just write this machine's report, to build for it elsewhere":
        'Nenhuma: só salvar o relatório desta máquina, para gerar a EFI em outro lugar',
    'Where should the report go?': 'Onde o relatório deve ser salvo?',
    'a path, or enter for {}': 'um caminho, ou Enter para {}',
    'Where is the report?': 'Onde está o relatório?',
    'a path, or enter to answer the questions instead': 'um caminho, ou Enter para responder as perguntas',
    'Use what was detected, or answer for yourself?': 'Usar o que foi detectado ou responder você mesmo?',
    'Use it: {}': 'Usar: {}',
    'Answer the questions myself': 'Responder as perguntas eu mesmo',
    'the profile questions are answered; everything below is still asked':
        'as perguntas do perfil estão respondidas; todo o resto abaixo ainda será perguntado',
    'What kind of machine is this?': 'Que tipo de máquina é esta?',
    'Desktop': 'Desktop',
    'Laptop': 'Notebook',
    'Which CPU vendor?': 'Qual o fabricante do processador?',
    'laptop profiles cover Intel only, so no vendor question':
        'os perfis de notebook só cobrem Intel, então não há pergunta de fabricante',
    'Which CPU generation?': 'Qual a geração do processador?',
    'How many physical cores?': 'Quantos núcleos físicos?',
    '{} cores': '{} núcleos',
    'Board or laptop brand?': 'Marca da placa-mãe ou do notebook?',
    'Which macOS are you installing?': 'Qual macOS você vai instalar?',
    'no board overlay': 'sem ajuste de placa',
    'Legacy BIOS': 'BIOS legado',
    'Which {} does that machine have?': 'Qual {} aquela máquina tem?',
    'none, or I do not know': 'nenhum, ou não sei',
    'These come from what this repository ships drivers for. Pick what that':
        'Estas opções vêm dos drivers que este repositório inclui. Escolha o que aquela',
    'machine has; anything else is left out rather than guessed at.':
        'máquina tem; o resto fica de fora em vez de ser adivinhado.',
    'Add these to the EFI?': 'Adicionar estes à EFI?',
    'Yes, for every macOS version they support': 'Sim, para todas as versões do macOS que eles suportam',
    'Yes, for one macOS version only': 'Sim, só para uma versão do macOS',
    'No, leave them out': 'Não, deixar de fora',
    'Work out the SSDTs for this machine?': 'Gerar os SSDTs para esta máquina?',
    "No, the profile's generic SSDTs will do": 'Não, os SSDTs genéricos do perfil bastam',
    'Open SSDTTime to work through those too?': 'Abrir o SSDTTime para resolver esses também?',
    'No, what came out is enough': 'Não, o que saiu já basta',
    'Yes, open the menus': 'Sim, abrir os menus',
    'SSDTTime is waiting for an answer': 'O SSDTTime está esperando uma resposta',
    "from SSDTTime's own menu, above": 'do próprio menu do SSDTTime, acima',
    'Map the USB ports now?': 'Mapear as portas USB agora?',
    'Yes, run USBToolBox': 'Sim, rodar o USBToolBox',
    'No, use UTBDefault and map later': 'Não, usar o UTBDefault e mapear depois',
    'Which framebuffer id?': 'Qual id de framebuffer?',
    'leave the key out; WhateverGreen picks': 'deixar a chave de fora; o WhateverGreen escolhe',
    'Fake the device-id?': 'Falsificar o device-id?',
    'Fake it to {}': 'Falsificar para {}',
    'Fake it to {} - reported, not stated by WhateverGreen': 'Falsificar para {} (relatado, não declarado pelo WhateverGreen)',
    'No, leave it as the machine reports it': 'Não, deixar como a máquina informa',
    'Set the trackpad up for SMBus?': 'Configurar o trackpad para SMBus?',
    'Yes, as the project says': 'Sim, como o projeto indica',
    'No, VoodooPS2 alone': 'Não, só o VoodooPS2',
    'Claim a Mac that is served {} {} instead?': 'Fingir ser um Mac que recebe o {} {} em vez disso?',
    'No, keep {} and let the install refuse': 'Não, manter {} e deixar a instalação recusar',
    'Press enter to close.': 'Aperte Enter para fechar.',

    # ---- setup.py: what it says -------------------------------------------
    'this machine': 'esta máquina',
    'building for': 'gerando para',
    'building for:': 'gerando para:',
    'this machine:': 'esta máquina:',
    'the ids you passed': 'os ids que você passou',
    'taken:': 'tirado:',
    'graphics:': 'vídeo:',
    'ignored:': 'ignorado:',
    '(virtual display adapters, not graphics hardware)': '(adaptadores de vídeo virtuais, não hardware de vídeo)',
    'nothing here is in any table this repository has, so there is no summary to give':
        'nada aqui está em alguma tabela deste repositório, então não há resumo para mostrar',
    'could not read this machine; every question is still answerable':
        'não foi possível ler esta máquina; todas as perguntas ainda podem ser respondidas',
    'Hardware report': 'Relatório de hardware',
    'wrote {}': 'salvo em {}',
    'Copy it to the machine you build on and pass it back:':
        'Copie para a máquina onde você vai gerar a EFI e passe de volta:',
    'Copy {} to the machine you build on and pass {} back:':
        'Copie para a máquina onde você vai gerar a EFI e passe de volta:',
    'Nothing is known about that machine, so nothing is detected for it.':
        'Nada se sabe sobre aquela máquina, então nada é detectado para ela.',
    'Graphics, audio and the trackpad need a report taken there:':
        'Vídeo, áudio e trackpad precisam de um relatório tirado lá:',
    'no {} overlay for this combination; using the generic profile':
        'sem ajuste {} para esta combinação; usando o perfil genérico',
    "reading this machine's ACPI tables": 'lendo as tabelas ACPI desta máquina',
    '{} tables in {}': '{} tabelas em {}',
    '{} more need an answer only you can give:': '{} precisam de uma resposta que só você pode dar:',
    'The laptop profiles already carry a generic XOSI and PNLF, so':
        'Os perfis de notebook já trazem um XOSI e um PNLF genéricos, então',
    'most machines need none of these.': 'a maioria das máquinas não precisa de nenhum destes.',
    '{} SSDTs and {} patches going in': '{} SSDTs e {} patches vão entrar',
    '{} SSDTs and {} patches': '{} SSDTs e {} patches',
    'written': 'gerado',
    'not needed': 'não necessário',
    'waiting on a choice': 'esperando uma escolha',
    'A machine usually needs a few SSDTs - a fake EC, PLUG for power':
        'Uma máquina costuma precisar de alguns SSDTs (um EC falso, PLUG para o gerenciamento',
    'management - and each is written against its own tables. SSDTTime':
        'de energia), e cada um é escrito a partir das tabelas dela. O SSDTTime',
    'does that and is bundled here. It works most of them out by itself;':
        'faz isso e vem incluído aqui. Ele resolve a maioria sozinho;',
    'the ones that need an answer are listed afterwards.':
        'os que precisam de resposta são listados depois.',
    "SSDTs need the target machine's ACPI tables. Take them there with":
        'Os SSDTs precisam das tabelas ACPI da máquina de destino. Tire elas lá com',
    'It opens in a window of its own; come back here when it closes.':
        'Ele abre numa janela própria; volte aqui quando ela fechar.',
    'The Mac this pretends to be': 'O Mac que esta máquina finge ser',
    '{} {} is past that. macOS decides from the identity, not from the hardware, so the install stops':
        'O {} {} passa disso. O macOS decide pela identidade, não pelo hardware, então a instalação para',
    'and does not say why.': 'e não diz o motivo.',
    'What changes with it: the identity drives power management, and some':
        'O que muda com isso: a identidade controla o gerenciamento de energia, e algumas',
    'releases hand a machine a different graphics path for it. It is a decision,':
        'versões dão um caminho de vídeo diferente para a máquina por causa dela. É uma decisão,',
    'which is why it is a question and not a fix.': 'por isso é uma pergunta e não uma correção.',
    'boot arguments needed: {}': 'argumentos de boot necessários: {}',
    'added to the config below': 'adicionados à config abaixo',
    'USB ports': 'Portas USB',
    'USB port map': 'Mapa de portas USB',
    'UTBDefault turns every port on without mapping any. A real map takes':
        'O UTBDefault liga todas as portas sem mapear nenhuma. Um mapa de verdade exige',
    'plugging a device into each port in turn, which USBToolBox does and this':
        'conectar um dispositivo em cada porta, uma por vez, o que o USBToolBox faz e este',
    'cannot - so it is here, and it can run now.': 'não consegue. Por isso ele vem junto e pode rodar agora.',
    'UTBDefault is going in, which turns every port on without mapping any.':
        'O UTBDefault vai entrar, o que liga todas as portas sem mapear nenhuma.',
    'That boots. It is not the same as a map, and sleep and USB 3 ports are':
        'Isso inicia. Não é o mesmo que um mapa, e a suspensão e as portas USB 3 são',
    'where the difference shows.': 'onde a diferença aparece.',
    'To make one: run USBToolBox on the target machine under Windows, plug a':
        'Para fazer um: rode o USBToolBox na máquina de destino pelo Windows, conecte um',
    'device into every port when it asks, and it writes a UTBMap.kext.':
        'dispositivo em cada porta quando ele pedir, e ele gera um UTBMap.kext.',
    'Then build again with --usb-map UTBMap.kext and it replaces the default.':
        'Depois gere de novo com --usb-map UTBMap.kext e ele substitui o padrão.',
    'It is bundled here: on Windows this builder offers to run it for you.':
        'Ele vem incluído aqui: no Windows, este construtor oferece rodá-lo para você.',
    '{}; UTBDefault stays in': '{}; o UTBDefault continua',
    '{} does not look like a kext': '{} não parece ser um kext',
    'Intel graphics framebuffer': 'Framebuffer do vídeo Intel',
    'none written: this iGPU has been reported not to accelerate, and a framebuffer id will not change that':
        'nenhum gerado: há relatos de que este iGPU não tem aceleração, e um id de framebuffer não muda isso',
    'The device-id this iGPU shows': 'O device-id que este iGPU mostra',
    '{} is not one {} supports as it stands.': '{} não é um que o {} suporte do jeito que está.',
    'WhateverGreen says:': 'O WhateverGreen diz:',
    'and the framebuffer that was reported with it, {}': 'e o framebuffer relatado junto com ele, {}',
    'Trackpad and keyboard': 'Trackpad e teclado',
    'on the PS/2 controller': 'no controlador PS/2',
    'pointing device': 'dispositivo apontador',
    "ignored: {}  (remote desktop input, not this machine's)": 'ignorado: {}  (entrada de área de trabalho remota, não desta máquina)',
    "(remote desktop input, not this machine's)": '(entrada de área de trabalho remota, não desta máquina)',
    'Windows named the SMBus controller after the driver bound to it, which':
        'O Windows deu ao controlador SMBus o nome do driver ligado a ele, o que',
    'is this machine saying the trackpad is on SMBus and not PS/2.':
        'é esta máquina dizendo que o trackpad está em SMBus e não em PS/2.',
    'Confirm it in macOS afterwards: "{}"': 'Confirme depois no macOS: "{}"',
    'no I2C controller here; if the trackpad turns out to be on SMBus, NEXT-STEPS.txt names the two kexts for that':
        'sem controlador I2C aqui; se o trackpad estiver em SMBus, o NEXT-STEPS.txt indica os dois kexts para isso',
    "{} kexts in the order the project gives, and {} of the profile's turned off:":
        '{} kexts na ordem que o projeto indica, e {} do perfil desligados:',
    "NVMeFix improves Apple's NVMe driver for third-party SSDs; adding it":
        'O NVMeFix melhora o driver NVMe da Apple para SSDs de outras marcas; adicionando ele',
    'Apple NVMe, which is the case NVMeFix is not for': 'NVMe da Apple, que é o caso para o qual o NVMeFix não serve',
    'Camera and card reader': 'Câmera e leitor de cartão',
    'on USB': 'em USB',
    'not on USB': 'fora do USB',
    'card reader': 'leitor de cartão',
    'a USB camera is handled by the class driver macOS already has, so it usually needs nothing':
        'uma câmera USB é atendida pelo driver genérico que o macOS já tem, então normalmente não precisa de nada',
    'a camera that is not on USB is an IPU or MIPI sensor, which macOS has no driver for':
        'uma câmera fora do USB é um sensor IPU ou MIPI, para o qual o macOS não tem driver',
    'beyond that this repository has no support data for these, so nothing is claimed or added':
        'além disso, este repositório não tem dados de suporte para estes, então nada é prometido ou adicionado',
    'Network kexts': 'Kexts de rede',
    'Intel Wi-Fi is built separately for each macOS release; using {} {}, which you named above.':
        'O Wi-Fi Intel é compilado separadamente para cada versão do macOS; usando {} {}, que você escolheu acima.',
    'Copy the': 'Copie a pasta',
    'folder from': 'de',
    'to the EFI partition of your USB drive.': 'para a partição EFI do seu pendrive.',
    'ROM is still a placeholder - set it to your own MAC address, see the README Post Installation section.':
        'A ROM ainda é um valor provisório: coloque o endereço MAC da sua placa de rede (veja a seção Pós-instalação do README).',
    'Follow-up for this EFI': 'Próximos passos para esta EFI',
    '--answers ran out: this run asks more questions than it was given':
        '--answers acabou: esta execução faz mais perguntas do que respostas foram dadas',
    'no profile for {}': 'nenhum perfil para {}',
    'no profiles for {}': 'nenhum perfil para {}',
    'all good': 'tudo certo',
    '{} macOS versions': '{} versões do macOS',

    # ---- setup.py, the console's own marks ---------------------------------
    'detected: {}': 'detectado: {}',
    '<- detected': '<- detectado',
    'Building': 'Gerando',
    'Storage': 'Disco',
    'no board overlay': 'sem ajuste de placa',
    'Copy the EFI folder from {} to the EFI partition of your USB drive.':
        'Copie a pasta EFI de {} para a partição EFI do seu pendrive.',
    '({}, {} on the PS/2 controller)': '({}, {} no controlador PS/2)',
    '({}, {})': '({}, {})',
    'pointing device': 'dispositivo apontador',
    'keyboard': 'teclado',
    'camera': 'câmera',

    # ---- build.py, the summary at the end --------------------------------
    'profiles': 'perfis',
    'payload': 'conteúdo',
    '{} items': '{} itens',
    'notes': 'notas',
    'output': 'saída',
    'warning': 'aviso',
    'added kexts': 'kexts adicionados',
    'tested {}': 'testado {}',
    'clean': 'sem problemas',

    # ---- audio.py ------------------------------------------------------------
    'Audio needs a layout-id, and which one works depends on the':
        'O áudio precisa de um layout-id, e qual funciona depende da',
    'machine rather than the codec. The config was built with the':
        'máquina e não do codec. A config foi gerada com o',
    'first of these. If sound does not work, or some ports do not,':
        'primeiro destes. Se o som não funcionar, ou algumas saídas não funcionarem,',
    'change alcid= in boot-args to the next one and reboot.':
        'troque o alcid= nos boot-args pelo próximo e reinicie.',
    'no audio codec was readable here': 'nenhum codec de áudio pôde ser lido aqui',
    '<- starting with this one': '<- começando por este',
    'and {} more, written to NEXT-STEPS.txt': 'e mais {}, anotados no NEXT-STEPS.txt',
    "no audio codec here is in AppleALC's list ({})": 'nenhum codec de áudio daqui está na lista do AppleALC ({})',

    # ---- gpu.py --------------------------------------------------------------
    'supported with a device-id spoof': 'suportado com um spoof de device-id',
    'should work, but nobody has reported it': 'deve funcionar, mas ninguém relatou ainda',
    'no driver was ever written for this family': 'nunca foi escrito um driver para esta família',
    'Intel iGPU, {}': 'iGPU Intel, {}',
    'no graphics hardware was readable here': 'nenhum hardware de vídeo pôde ser lido aqui',
    'no table here claims this card, so nothing is added for it':
        'nenhuma tabela aqui dá suporte a esta placa, então nada é adicionado para ela',
    'the rest of the build applies as normal; this is the graphics only':
        'o resto da geração segue normalmente; isto vale só para o vídeo',
    'needs boot argument {}': 'precisa do argumento de boot {}',
    'needs {}': 'precisa de {}',
    'a supported card would be AMD Polaris, Vega or Navi 10/21/23':
        'uma placa com suporte seria AMD Polaris, Vega ou Navi 10/21/23',
    'whether it is supported is answered by {}': 'quem responde se tem suporte é {}',
    'AMD integrated graphics are not covered by this repository':
        'o vídeo integrado da AMD não é coberto por este repositório',
    'you can disable it and use {} instead, which is supported':
        'você pode desativá-la e usar {} no lugar, que tem suporte',
    'the integrated GPU is not supported either, so there is nothing to fall back to':
        'o vídeo integrado também não tem suporte, então não há alternativa',
    '{} is not among the ids this generation supports without a faked device-id':
        '{} não está entre os ids que esta geração suporta sem falsificar o device-id',
    "the kexts that drive them are {}'s work": 'os kexts que controlam elas são trabalho de {}',
    'whether the integrated GPU can be used instead could not be determined':
        'não foi possível saber se o vídeo integrado pode ser usado no lugar',
    'there is no integrated GPU here to fall back to': 'não há vídeo integrado aqui para usar no lugar',
    '{}, natively supported': '{}, suportado nativamente',
    '{}, not natively': '{}, não nativamente',
    '{}, which the guide lists as unsupported': '{}, que o guia lista como sem suporte',
    '({})': '({})',

    # ---- igpu.py -------------------------------------------------------------
    'boots without graphics acceleration': 'inicia sem aceleração de vídeo',
    'default': 'padrão',
    'recommended': 'recomendado',
    '{} connectors, {}': '{} conectores, {}',
    '{} connectors, {} MB': '{} conectores, {} MB',
    'headless, {}': 'sem saída de vídeo, {}',
    'headless, {} MB': 'sem saída de vídeo, {} MB',
    "not a real framebuffer: nothing claims it, so none attaches. Reported by this repository's maintainer as a way to get a first boot before the right id is known.":
        'não é um framebuffer de verdade: nada o reconhece, então nenhum é ligado. Relatado pelo mantenedor deste repositório como um jeito de conseguir o primeiro boot antes de saber o id certo.',
    'The framebuffer id decides which ports light up and how much':
        'O id de framebuffer decide quais saídas de vídeo funcionam e quanta',
    'memory the iGPU gets. {} went in. If the screen stays':
        'memória o iGPU recebe. {} foi usado. Se a tela ficar',
    'black, or an HDMI or DisplayPort output does nothing, try the next:':
        'preta, ou uma saída HDMI ou DisplayPort não funcionar, tente o próximo:',
    'Leaving the key out entirely is the other option: WhateverGreen':
        'Deixar a chave totalmente de fora é a outra opção: o WhateverGreen',
    'then injects the default framebuffer for the generation.':
        'então injeta o framebuffer padrão da geração.',
    'Change it under DeviceProperties in config.plist, at':
        'Mude em DeviceProperties no config.plist, em',
    '{}, key AAPL,ig-platform-id. The data value is the': '{}, chave AAPL,ig-platform-id. O valor é a',
    'byte-swapped form shown above.': 'forma com os bytes invertidos mostrada acima.',
    'Beyond this id, laptops often need connector patches tuned by hand.':
        'Além deste id, notebooks muitas vezes precisam de patches de conector ajustados à mão.',
    'This builder does not write those:': 'Este construtor não gera esses:',
    '{} framebuffer ids for this generation, starting with {}': '{} ids de framebuffer para esta geração, começando por {}',
    '{} framebuffer id for this generation, starting with {}': '{} id de framebuffer para esta geração, começando por {}',
    'and {} more, in NEXT-STEPS.txt': 'e mais {}, no NEXT-STEPS.txt',
    'nothing to offer': 'nada a oferecer',

    # ---- smbios.py -----------------------------------------------------------
    'served up to {}': 'recebe até o {}',
    '{} is not in the model table': '{} não está na tabela de modelos',
    "no board of {} is in macrecovery's list": 'nenhuma placa de {} está na lista do macrecovery',
    'whatever Apple is serving now': 'o que a Apple estiver oferecendo agora',
    'one Apple keeps current, so whatever is newest': 'uma que a Apple mantém atualizada, então o mais novo que houver',

    # ---- inputdev.py ---------------------------------------------------------
    'an I2C controller is present  [{}]': 'há um controlador I2C  [{}]',
    'No I2C controller was found, so nothing was added for the trackpad.':
        'Nenhum controlador I2C foi encontrado, então nada foi adicionado para o trackpad.',
    'A laptop keyboard is almost always PS/2 and VoodooPS2 is already in':
        'O teclado de um notebook quase sempre é PS/2, e o VoodooPS2 já está no',
    'the profile, which usually brings the trackpad with it.': 'perfil, o que normalmente já traz o trackpad junto.',
    'If the trackpad still does nothing, it may be on SMBus instead:':
        'Se o trackpad continuar sem funcionar, ele pode estar em SMBus:',
    'Neither kext is added automatically: nothing this reads says which':
        'Nenhum dos kexts é adicionado automaticamente: nada do que é lido diz em qual',
    'bus a trackpad is on, and adding the wrong one is not harmless.':
        'barramento o trackpad está, e adicionar o errado não é inofensivo.',
    'An I2C controller was found, so VoodooI2C and VoodooI2CHID went in.':
        'Um controlador I2C foi encontrado, então o VoodooI2C e o VoodooI2CHID foram incluídos.',
    'VoodooI2CHID covers I2C-HID trackpads, which is most of them. If the':
        'O VoodooI2CHID atende trackpads I2C-HID, que são a maioria. Se o',
    'trackpad still does nothing, the release carries a plugin per family:':
        'trackpad continuar sem funcionar, a versão traz um plugin por família:',
    'If it is not I2C at all, these are the other two paths:': 'Se não for I2C, estes são os outros dois caminhos:',
    'Some trackpads also need an SSDT before macOS will see them at all.':
        'Alguns trackpads também precisam de um SSDT para o macOS enxergá-los.',
    'That is machine-specific and not something this builder can write:':
        'Isso depende de cada máquina e este construtor não consegue gerar:',
    'https://voodooi2c.github.io/ has the procedure.': 'https://voodooi2c.github.io/ tem o procedimento.',
    'a PS/2 device is present too, so the trackpad may well be PS/2 and this unnecessary':
        'também há um dispositivo PS/2, então o trackpad pode muito bem ser PS/2 e isto ser desnecessário',
    'no I2C controller here': 'sem controlador I2C aqui',

    # ---- summary.py: what the hardware means ------------------------------
    'Hardware for macOS': 'Hardware para o macOS',
    'from {}': 'de {}',
    'report {}': 'relatório {}',
    '{} sets the oldest, {} the newest': '{} define o mais antigo, {} o mais novo',
    'Graphics': 'Vídeo', 'Audio': 'Áudio', 'Storage': 'Disco', 'Camera': 'Câmera',
    'Card reader': 'Leitor de cartão',
    'kaby-lake, laptop profile': 'kaby-lake, perfil de notebook',
    '{}, laptop profile': '{}, perfil de notebook',
    '{}, desktop profile': '{}, perfil de desktop',
    '{} layouts to try': '{} layouts para testar',
    '{}, natively supported': '{}, suportado nativamente',
    'supported': 'suportado',
    'driven by macOS': 'controlado pelo macOS',
    'not supported': 'sem suporte',
    'unknown': 'desconhecido',
    'not present': 'ausente',
    '{} or newer': '{} ou mais novo',
    'not readable': 'não legível',
    'answer the question by hand': 'responda a pergunta manualmente',
    'Apple silicon, running macOS natively; this program builds for Intel and AMD':
        'Apple silicon, rodando macOS nativamente; este programa gera para Intel e AMD',
    'this generation is not one the decoder recognises': 'esta geração não é reconhecida pelo decodificador',
    'not in the card table or the iGPU list': 'não está na tabela de placas nem na lista de iGPUs',
    'macOS drives these; there is no HD audio codec to match': 'o macOS controla estes; não há codec de áudio HD para associar',
    'no codec readable': 'nenhum codec legível',
    'no AppleALC layout names this codec': 'nenhum layout do AppleALC cita este codec',
    'AppleALC, {} layout': 'AppleALC, layout {}',
    'one build per macOS': 'uma compilação por macOS',
    'no NVMe': 'sem NVMe',
    'nothing to add': 'nada a adicionar',
    'macOS drives it': 'o macOS controla',
    'on PS/2; VoodooPS2Controller is in the laptop profile': 'em PS/2; o VoodooPS2Controller está no perfil de notebook',
    'no I2C controller and nothing on PS/2': 'sem controlador I2C e nada em PS/2',
    '{} is not supported and there is no integrated graphics to fall back on. The card has to be replaced with one macOS drives, or this machine has no display under macOS.':
        '{} não tem suporte e não há vídeo integrado para usar no lugar. A placa precisa ser trocada por uma que o macOS reconheça, ou esta máquina fica sem imagem no macOS.',
    '{} is not supported. macOS would run on {} instead, so the range above still holds - but the card gives you nothing and the display has to come off the integrated one.':
        '{} não tem suporte. O macOS rodaria no {}, então a faixa acima continua valendo, mas a placa não serve para nada e a imagem tem que sair pelo vídeo integrado.',
    '{} is not supported, and neither is {}. The card has to be replaced with one macOS drives; the integrated graphics cannot cover for it.':
        '{} não tem suporte, e o {} também não. A placa precisa ser trocada por uma que o macOS reconheça; o vídeo integrado não consegue substituí-la.',
    '{} is in neither the card table nor the family rules, so nothing here can say whether macOS drives it. That is not the same as unsupported.':
        '{} não está na tabela de placas nem nas regras de família, então nada aqui sabe dizer se o macOS reconhece. Isso não é o mesmo que sem suporte.',
    'macOS does not support {} of these: {}.': 'O macOS não suporta {} destes: {}.',
    'For a card in a slot, replacing it is usually the answer. For one soldered on,':
        'Para uma placa encaixada num slot, trocar costuma ser a solução. Para uma soldada,',
    'it is something to live without. Either way this does not stop the build, and the':
        'é algo para viver sem. De qualquer forma isso não impede a geração, e as',
    'sections below say more.': 'seções abaixo explicam mais.',
    'Nothing here is known to be unsupported.': 'Nada aqui é sabidamente sem suporte.',
    '{} left as unknown, where no table here has anything to say.':
        '{} ficaram como desconhecidos, porque nenhuma tabela aqui tem algo a dizer.',
    'from the parts these tables bound. The SMBIOS a build picks has a ceiling':
        'a partir das peças que essas tabelas limitam. O SMBIOS escolhido na geração tem um teto',
    'of its own, and so can a discrete card; neither is recorded here.':
        'próprio, e uma placa de vídeo dedicada também pode ter; nenhum dos dois está registrado aqui.',
    'part of the Apple silicon package, driven by macOS': 'parte do chip Apple silicon, controlado pelo macOS',
    '{}, reported by {}': '{}, relatado por {}',
    'none readable': 'nenhum legível',
    'nothing was reported on the graphics bus': 'nada foi informado no barramento de vídeo',
    'no HD audio codec on this machine': 'sem codec de áudio HD nesta máquina',
    'up to {}': 'até {}',
    'no macOS range documented': 'sem faixa de macOS documentada',
    '+{} by macOS version': '+{} por versão do macOS',
    'on PS/2': 'em PS/2',
    'the kernel patches this CPU needs': 'os patches de kernel que este processador precisa',
    'macOS has it on {}': 'o macOS tem em {}',
    "a Mac's own camera, which this repository has no data for either way":
        'a câmera do próprio Mac, sobre a qual este repositório não tem dados',
    'USB, so the class driver macOS has handles it': 'USB, então o driver genérico do macOS atende',
    'not on USB, so an IPU or MIPI sensor': 'fora do USB, então é um sensor IPU ou MIPI',
    '{} sets the oldest': '{} define o mais antigo',
    '{} lists it and does not drive it yet': '{} lista ele mas ainda não o controla',
    'not in the one driver this repository has data for': 'não está no único driver sobre o qual este repositório tem dados',
    'this Mac has no such device': 'este Mac não tem esse dispositivo',
    'this machine says what the device is; no kext here claims it':
        'esta máquina diz que dispositivo é; nenhum kext aqui dá suporte a ele',
    'nothing recognised': 'nada reconhecido',
    'no kext here claims a device on this machine': 'nenhum kext aqui dá suporte a um dispositivo desta máquina',
    'no devices readable': 'nenhum dispositivo legível',
    'the machine says what it is; nothing here drives it': 'a máquina diz o que é; nada aqui controla',
    'no {} profile for {}': 'nenhum perfil {} para {}',

    # ---- advise.py ----------------------------------------------------------
    'Network hardware': 'Hardware de rede',
    'from {}: {} PCI, {} USB devices': 'de {}: {} dispositivos PCI, {} USB',
    'This is a report. Nothing was added to any config.': 'Isto é um relatório. Nada foi adicionado a nenhuma config.',
    'nothing was readable here.': 'nada pôde ser lido aqui.',
    'On a Hackintosh target run this from Windows or Linux;': 'Na máquina Hackintosh de destino, rode isto pelo Windows ou Linux;',
    'a Mac reports its own hardware, not the machine you are building for.':
        'um Mac informa o próprio hardware, não o da máquina para a qual você está gerando.',
    'Some devices match more than one kext, because they target different':
        'Alguns dispositivos combinam com mais de um kext, porque eles atendem versões',
    'macOS versions. setup.py can add them all with their version bounds, or':
        'diferentes do macOS. O setup.py pode adicionar todos com seus limites de versão, ou',
    'just the ones for a single release.': 'só os de uma versão.',
    'no device here is claimed by any kext this repository knows.':
        'nenhum dispositivo aqui é atendido por um kext que este repositório conheça.',
    'That means either the device is supported by macOS with no kext at all,':
        'Isso quer dizer que ou o dispositivo é suportado pelo macOS sem kext nenhum,',
    'or it is not supported. Check {}': 'ou não tem suporte. Confira {}',
    'no macOS range is documented for this id; the kext matches it, and nothing here states how far it reaches':
        'não há faixa de macOS documentada para este id; o kext combina com ele, e nada aqui diz até onde ele vai',
    'but not on the macOS you asked for: this stops at {}': 'mas não no macOS que você pediu: este para no {}',
    'up to {}; above that see the note in data/network.toml': 'até {}; acima disso veja a nota em data/network.toml',

    # ---- build.py -----------------------------------------------------------
    'identity left as a placeholder; set it before signing in to iCloud':
        'identidade deixada como provisória; defina antes de entrar no iCloud',
    'macserial not available for this platform; identity left as a placeholder':
        'macserial não disponível nesta plataforma; identidade deixada como provisória',
    'macserial produced nothing for {}; identity left as a placeholder':
        'o macserial não gerou nada para {}; identidade deixada como provisória',
    'ocvalidate not available for this platform; config was not validated':
        'ocvalidate não disponível nesta plataforma; a config não foi validada',
    'No issues found': 'Nenhum problema encontrado',
    'added kexts': 'kexts adicionados',
    'referenced but missing from the repository: {}': 'citado mas ausente do repositório: {}',
    'no {} profile named {}; it was ignored': 'nenhum perfil {} chamado {}; foi ignorado',
    '{} ACPI patches were already in the config and were not added twice':
        '{} patches ACPI já estavam na config e não foram adicionados de novo',
    'load order: {} needs {}, which {}': 'ordem de carregamento: {} precisa de {}, que {}',
    '{} disabled: the kext replacing it says it must not load too':
        '{} desativado: o kext que o substitui diz que os dois não podem carregar juntos',
    '{} replaced by the one built for this machine': '{} substituído pelo gerado para esta máquina',
    '{} disabled: {} is built for this machine and does the same job':
        '{} desativado: {} foi gerado para esta máquina e faz o mesmo trabalho',
    'identity     {} -> {}, asked for': 'identidade   {} -> {}, a pedido',

    # ---- stick.py -------------------------------------------------------------
    'Removable disks': 'Discos removíveis',
    'The disk this computer booted from is not in this list, and cannot be.':
        'O disco de onde este computador iniciou não está nesta lista e nunca vai estar.',
    'none. Plug one in, or the disk you mean is not removable - this only ever lists removable, external, physical disks, and never the one this computer booted from.':
        'nenhum. Conecte um, ou o disco que você quer não é removível: aqui só aparecem discos físicos, externos e removíveis, e nunca o disco de onde este computador iniciou.',
    'It is one of {} partitions on the stick.': 'É uma das {} partições do pendrive.',
    'FAT32 with {} free, so this can be written to - though the partition scheme is {} rather than GPT, which is what the guide expects.{}':
        'FAT32 com {} livres, então dá para gravar, mas o esquema de partição é {} em vez de GPT, que é o que o guia espera.{}',
    'this holds {}, and OpenCore boots from a FAT32 partition. It has to be erased and formatted first.':
        'este tem {}, e o OpenCore inicia de uma partição FAT32. Ele precisa ser apagado e formatado primeiro.',
    'the only FAT partition on it is {} - a helper partition, not one an EFI and an installer fit on. It has to be erased and formatted first.':
        'a única partição FAT nele é {}, uma partição auxiliar onde não cabem uma EFI e um instalador. Ele precisa ser apagado e formatado primeiro.',
    'the FAT32 partition on it is not mounted, so there is nowhere to copy to. Mount it, or format the stick.':
        'a partição FAT32 dele não está montada, então não há para onde copiar. Monte ela ou formate o pendrive.',
    '{} is FAT32 but has {} free, and a recovery installer is about 700 MB.{} Erase the stick, or clear it.':
        '{} é FAT32 mas tem {} livres, e um instalador recovery tem uns 700 MB.{} Apague o pendrive ou libere espaço.',
    'FAT32 under GPT with {} free: ready as it is, nothing to erase.{}':
        'FAT32 em GPT com {} livres: pronto do jeito que está, nada a apagar.{}',
    '{} is not a folder this can write to': '{} não é uma pasta onde dê para gravar',
    'nothing was named to copy': 'nada foi indicado para copiar',
    '{} is not one of the removable disks this can write to, so it will not be erased':
        '{} não é um dos discos removíveis onde dá para gravar, então não será apagado',
    '{} is not one of the removable disks this can write to': '{} não é um dos discos removíveis onde dá para gravar',
    'erasing a disk needs root on Linux, and this does not ask for it. Run: sudo sgdisk --zap-all /dev/{} && sudo sgdisk -n 1:0:0 -t 1:0700 /dev/{} && sudo mkfs.vfat -F 32 -n {} /dev/{}1':
        'apagar um disco no Linux precisa de root, e este programa não pede. Rode: sudo sgdisk --zap-all /dev/{} && sudo sgdisk -n 1:0:0 -t 1:0700 /dev/{} && sudo mkfs.vfat -F 32 -n {} /dev/{}1',
    'erasing a disk needs an administrator on Windows, and this is not running as one. Open diskpart as administrator: select disk {}, clean, convert gpt, create partition primary, format fs=fat32 quick label={}, assign':
        'apagar um disco no Windows precisa de administrador, e este programa não está rodando como um. Abra o diskpart como administrador: select disk {}, clean, convert gpt, create partition primary, format fs=fat32 quick label={}, assign',
    'no way to erase a disk on {}': 'não há como apagar um disco no {}',
    'the tool that does this is not on this machine': 'a ferramenta que faz isso não está nesta máquina',
    'nothing here lists disks on {}': 'nada aqui lista discos no {}',
    'This erases everything on it.': 'Isto apaga tudo nele.',
    'Written to {}': 'Gravado em {}',
    '{} has no BOOT/BOOTx64.efi in it, so it is not an EFI folder OpenCore would boot':
        '{} não tem BOOT/BOOTx64.efi, então não é uma pasta EFI que o OpenCore iniciaria',
    '{} holds no BaseSystem, so there is no installer here to copy': '{} não tem BaseSystem, então não há instalador aqui para copiar',
    '--list says which are': '--list mostra quais são',
    'erased and formatted': 'apagado e formatado',
    '{} is there, so this stick boots': '{} está lá, então este pendrive inicia',
    'no {} here yet - copy the EFI folder too, or this will not boot':
        'ainda não há {} aqui: copie a pasta EFI também, ou ele não vai iniciar',
    'write to {}': 'gravar em {}',
    'mounted at {}': 'montado em {}',
    'nothing was erased': 'nada foi apagado',
    'type {} to go ahead:': 'digite {} para continuar:',
    'it exited {}': 'terminou com o código {}',
    'diskutil did not answer': 'o diskutil não respondeu',
    'lsblk did not answer': 'o lsblk não respondeu',
    'Get-Disk did not answer; it needs the Storage module': 'o Get-Disk não respondeu; ele precisa do módulo Storage',

    # ---- recovery.py ----------------------------------------------------------
    "these boards are kept current, so this row asks for whatever macOS is newest rather than for a version. boards.json does not name it; data/mac.toml does, from Apple's own metadata, and it said {} {} when that table was last refreshed. Press the button to ask Apple for today's answer.":
        'estas placas são mantidas atualizadas, então esta linha pede o macOS mais novo que houver, e não uma versão. O boards.json não diz qual é; o data/mac.toml diz, a partir dos dados da própria Apple, e indicava {} {} quando a tabela foi atualizada pela última vez. Clique no botão para perguntar à Apple a resposta de hoje.',
    'these boards are kept current, so this is the newest macOS Apple is serving today - the board list does not name it in advance, and neither does this':
        'estas placas são mantidas atualizadas, então este é o macOS mais novo que a Apple está oferecendo hoje; a lista de placas não diz qual é com antecedência, e este programa também não',
    'the board list records {} as the newest this board reaches. The image Apple hands back is some build of {}; recovery downloads the rest during the install.':
        'a lista de placas registra {} como o mais novo que esta placa alcança. A imagem que a Apple devolve é alguma compilação do {}; o recovery baixa o resto durante a instalação.',
    'Whatever Apple serves now': 'O que a Apple oferecer agora',
    '{}, {} files, {} MB': '{}, {} arquivos, {} MB',
    'Fetching {} from Apple': 'Baixando {} da Apple',
    'board {}, serial {}, into {}': 'placa {}, serial {}, em {}',
    'OpenCore lists it at the boot menu; it needs a wired connection or a':
        'O OpenCore mostra ele no menu de inicialização; precisa de conexão por cabo ou de uma',
    'card macOS already drives, because the rest of macOS comes down during':
        'placa que o macOS já reconheça, porque o resto do macOS é baixado durante',
    'the install.': 'a instalação.',
    'Nothing here recognised the network hardware in this machine, so whether recovery can download during the install is not something this can answer. It needs a card macOS drives, on the machine being installed.':
        'Nada aqui reconheceu o hardware de rede desta máquina, então não dá para dizer se o recovery consegue baixar durante a instalação. Ele precisa de uma placa que o macOS reconheça, na máquina que está sendo instalada.',
    'No hardware report, so nothing here knows whether the machine being installed has a network card macOS drives. Recovery downloads macOS on that machine; if it cannot reach the network, it boots and stops.':
        'Sem relatório de hardware, nada aqui sabe se a máquina que vai ser instalada tem uma placa de rede que o macOS reconheça. O recovery baixa o macOS naquela máquina; se não conseguir acessar a rede, ele inicia e para.',
    'Wi-Fi on this machine has a macOS driver, so recovery can connect and download during the install.':
        'O Wi-Fi desta máquina tem driver no macOS, então o recovery consegue se conectar e baixar durante a instalação.',
    '{}, but its Ethernet is driven. Recovery will work - plug in an Ethernet cable before you start the install. The download happens on this machine, and Wi-Fi will not be there to carry it.':
        '{}, mas a Ethernet dela é reconhecida. O recovery vai funcionar: conecte um cabo de rede antes de começar a instalação. O download acontece nesta máquina, e o Wi-Fi não vai estar disponível.',
    'Neither the Wi-Fi nor the Ethernet in this machine has a macOS driver here. Recovery would boot and then have nothing to download over: use a whole macOS image instead, or fit a card that is supported.':
        'Nem o Wi-Fi nem a Ethernet desta máquina têm driver no macOS aqui. O recovery iniciaria e não teria por onde baixar: use uma imagem completa do macOS ou instale uma placa com suporte.',
    'No network card was found on this machine at all. Recovery downloads macOS during the install and cannot do it without one: use a whole macOS image instead.':
        'Nenhuma placa de rede foi encontrada nesta máquina. O recovery baixa o macOS durante a instalação e não consegue sem uma: use uma imagem completa do macOS.',
    'The Wi-Fi card in this machine has no macOS driver here': 'A placa Wi-Fi desta máquina não tem driver no macOS aqui',
    'This machine has no Wi-Fi card': 'Esta máquina não tem placa Wi-Fi',
    'Nothing here recognises the Wi-Fi in this machine': 'Nada aqui reconhece o Wi-Fi desta máquina',
    'Apple answered, and listed no macOS in it': 'A Apple respondeu, mas não listou nenhum macOS',
    'no macrecovery is vendored, so there is nothing to drive': 'o macrecovery não está incluído, então não há o que rodar',
    'no macrecovery is vendored': 'o macrecovery não está incluído',
    "the tool could not verify what it downloaded against Apple's chunklist, so the bytes are not the ones Apple sent; downloading it again is the fix":
        'a ferramenta não conseguiu conferir o download com a chunklist da Apple, então os dados não são os que a Apple mandou; baixar de novo resolve',
    'the download reported success but wrote nothing': 'o download disse que deu certo mas não gravou nada',
    'Recovery installers Apple will serve': 'Instaladores recovery que a Apple oferece',
    "The number is what the board list records as that board's newest, not":
        'O número é o que a lista de placas registra como o mais novo daquela placa, não',
    'the image Apple hands back: asked for the 12.7.6 board it served a 12.6':
        'a imagem que a Apple devolve: pedindo a placa do 12.7.6, ela mandou um BaseSystem',
    'BaseSystem. Recovery downloads the rest during the install.':
        '12.6. O recovery baixa o resto durante a instalação.',
    "Read from macrecovery's own boards.json. Ask for one by version, by name,":
        'Lido do boards.json do próprio macrecovery. Peça um pela versão, pelo nome',
    "or 'latest'.": "ou 'latest'.",
    '{} is not one of the versions macrecovery lists': '{} não é uma das versões que o macrecovery lista',
    '{} already holds {}': '{} já contém {}',
    'delete them first; this will not overwrite a download somebody may be part way through':
        'apague eles primeiro; este programa não sobrescreve um download que alguém pode estar no meio',
    'Apple could not be asked: {}': 'Não foi possível consultar a Apple: {}',
    'the download stopped: {}': 'o download parou: {}',
    'the download finished and then {} was not where it had been written. Something moved or renamed it while it ran - leave that folder alone until it finishes, and try again':
        'o download terminou e depois {} não estava onde tinha sido gravado. Algo moveu ou renomeou durante o processo: não mexa nessa pasta até terminar e tente de novo',

    # ---- installer.py ---------------------------------------------------------
    "This builds a macOS installer with Apple's own createinstallmedia, which only runs on macOS.":
        'Isto gera um instalador do macOS com o createinstallmedia da própria Apple, que só roda no macOS.',
    '{} is not a macOS installer app: it has no createinstallmedia in it':
        '{} não é um app instalador do macOS: não tem createinstallmedia dentro',
    'attached as {}': 'montado como {}',
    '{} is ready': '{} está pronto',
    'It is a flat sector image: rename it .raw or .img and balenaEtcher':
        'É uma imagem de setores: renomeie para .raw ou .img e o balenaEtcher',
    'writes it from Windows, Linux or macOS.': 'grava ela pelo Windows, Linux ou macOS.',
    '{} is already there; move it or pick another name': '{} já existe; mova ou escolha outro nome',
    'the image could not be made: {}': 'não foi possível criar a imagem: {}',
    'the image could not be attached: {}': 'não foi possível montar a imagem: {}',
    'the image could not be partitioned: {}': 'não foi possível particionar a imagem: {}',
    "nothing in hdiutil's answer looks like a disk: {}": 'nada na resposta do hdiutil parece um disco: {}',
    'no volume called {} is mounted': 'nenhum volume chamado {} está montado',
    'you cancelled the password prompt, so nothing was written': 'você cancelou o pedido de senha, então nada foi gravado',
    'the privileged step failed with nothing to say': 'a etapa com privilégios falhou sem dizer nada',
    'the app is           {}': 'o app tem            {}',
    'createinstallmedia wants about {} more': 'o createinstallmedia precisa de mais uns {}',
    'so the volume needs  {}': 'então o volume precisa de {}',
    'plus an EFI partition of {}': 'mais uma partição EFI de {}',
    'image: {} GiB': 'imagem: {} GiB',
    'hdiutil and du count in GiB; diskutil prints decimal GB, which is':
        'o hdiutil e o du contam em GiB; o diskutil mostra GB decimais, que é',
    'the same number said differently.': 'o mesmo número dito de outro jeito.',
    'partitioned {}: {} then {}': 'particionado {}: {} e depois {}',
    'This next part needs an administrator password': 'A próxima parte precisa da senha de administrador',
    'createinstallmedia blesses a volume and BootInstall writes a master':
        'o createinstallmedia marca um volume como inicializável e o BootInstall grava um registro',
    'boot record; neither can be done without it. Run it yourself with':
        'mestre de inicialização; nenhum dos dois funciona sem ela. Rode você mesmo com',
    '--script if you would rather.': '--script se preferir.',
    'put the EFI folder on {}': 'pasta EFI colocada em {}',

    # ---- acpi.py --------------------------------------------------------------
    'not needed on this machine': 'não necessário nesta máquina',
    'needs a choice': 'precisa de uma escolha',
    'a fake EC, or nothing if the machine has a real one': 'um EC falso, ou nada se a máquina tiver um de verdade',
    'plugin-type on the first CPU object': 'plugin-type no primeiro objeto de CPU',
    'the AWAC clock, if this board has one': 'o relógio AWAC, se a placa tiver um',
    'native NVRAM on a true 300-series board': 'NVRAM nativa numa placa série 300 de verdade',
    'IRQ conflicts, if there are any': 'conflitos de IRQ, se houver',
    'MCHC and BUS0, if there is a bus device': 'MCHC e BUS0, se houver um dispositivo de barramento',
    'laptop backlight; asks about the panel': 'brilho da tela do notebook; pergunta sobre o painel',
    'which Windows versions _OSI should answer to': 'a quais versões do Windows o _OSI deve responder',
    'USB power properties': 'propriedades de energia do USB',
    'reserved memory regions; asks which to drop': 'regiões de memória reservadas; pergunta quais descartar',
    'for USB port mapping, which is its own step': 'para o mapeamento de portas USB, que é uma etapa à parte',
    'needs the device path of the bridge to create': 'precisa do caminho do dispositivo da ponte a criar',
    'asks which bridge to define': 'pergunta qual ponte definir',
    '{} SSDTs and {} patches in {}': '{} SSDTs e {} patches em {}',
    '{} is missing': '{} não foi encontrado',
    '{} is not usable on {}': '{} não pode ser usado no {}',
    'SSDTTime is not usable on {}': 'o SSDTTime não pode ser usado no {}',
    'the working copy and the tables are the same folder ({}); the working copy is emptied first, so this would delete them':
        'a cópia de trabalho e as tabelas são a mesma pasta ({}); a cópia de trabalho é esvaziada antes, então isso apagaria as tabelas',
    'it wrote no Results folder': 'ele não gerou a pasta Results',
    'ACPI tables cannot be dumped from macOS': 'não dá para extrair as tabelas ACPI pelo macOS',
    'nothing was dumped': 'nada foi extraído',
    'SSDTTime stopped: {}': 'o SSDTTime parou: {}',
    'Empty it yourself or point somewhere else': 'Esvazie você mesmo ou indique outro lugar',
    'the tables could not be dumped without asking: {}': 'não deu para extrair as tabelas sem perguntar: {}',
    'the tables could not be loaded without asking: {}': 'não deu para carregar as tabelas sem perguntar: {}',
    'no ACPI tables were loaded, so there is nothing to read': 'nenhuma tabela ACPI foi carregada, então não há o que ler',
    '{} holds things a dump did not write ({});': '{} tem coisas que a extração não gerou ({});',
    'this looks like what an older build left here, so deleting the folder is safe.':
        'parece algo deixado por uma versão anterior, então é seguro apagar a pasta.',
    'not in this version of the tool': 'não existe nesta versão da ferramenta',

    # ---- usbmap.py ------------------------------------------------------------
    'build with: setup.py --usb-map {}': 'gere com: setup.py --usb-map {}',
    '{} is not here': '{} não está aqui',
    'no map was written': 'nenhum mapa foi gerado',
    'it is a Windows build, and this is {}': 'é uma versão para Windows, e este sistema é {}',

    # ---- detect.py ------------------------------------------------------------
    'unknown CPU': 'processador desconhecido',
    '{} does not exist': '{} não existe',
    '{} is not a hardware report; make one with "detect.py --report {}" on the machine you are building for':
        '{} não é um relatório de hardware; gere um com "detect.py --report {}" na máquina para a qual você vai gerar a EFI',
    '{} was written by a newer version of this tool (report {}, this one reads {})':
        '{} foi gerado por uma versão mais nova desta ferramenta (relatório {}, esta lê {})',
    '{} PCI, {} USB, {} audio ids': '{} ids PCI, {} USB, {} de áudio',
    '{} could not be read: {}': '{} não pôde ser lido: {}',
    'Copy it to the machine you build on and run:': 'Copie para a máquina onde você vai gerar a EFI e rode:',

    # ---- inventory.py and netkexts.py ---------------------------------------
    'the recovery installer on the Recovery tab, fetched from Apple only when asked for; and, on the same tab, asking Apple which macOS it is serving today, which is the one row the board table will not name':
        'o instalador recovery na aba Recovery, baixado da Apple só quando pedido; e, na mesma aba, a consulta à Apple sobre qual macOS ela está oferecendo hoje, que é a única linha que a tabela de placas não nomeia',
    'never supported': 'nunca suportado',
    'listed, not driven yet': 'listado, ainda não controlado',
    'every supported macOS': 'todos os macOS suportados',
    '{} needs a build for one specific macOS, so it cannot be added in the every-version mode':
        '{} precisa de uma compilação para um macOS específico, então não pode ser adicionado no modo de todas as versões',
}

# Only ever looked up by i18n.fmt() where the message is built. Matched after
# printing, each of these would also match sentences it was never meant for.
FMT = {
    '{} to {}': '{} até {}',
    '{} or newer': '{} ou mais novo',
}
