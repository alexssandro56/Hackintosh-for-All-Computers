// Português do Brasil. The key is the English text exactly as the code writes
// it; the value is what is shown instead. {0}, {1}… stay where they are.
using System.Collections.Generic;

namespace Shell.Engine;

public static partial class L
{
    static readonly Dictionary<string, string> Pt = new()
    {
        // ---- engine and session ------------------------------------------
        ["inside this app"] = "dentro deste app",
        ["beside this window"] = "ao lado desta janela",
        ["Found the engine at {0} but no Python that can run it. It needs 3.11 or newer, for tomllib."] =
            "O motor foi encontrado em {0}, mas nenhum Python capaz de rodá-lo. É preciso o 3.11 ou mais novo, por causa do tomllib.",
        ["a clone at "] = "um clone em ",
        ["No engine found. Looked for {0} beside this window, inside this app's Resources, and for tools/setup.py above {1}."] =
            "Nenhum motor encontrado. Procurei {0} ao lado desta janela, na pasta Resources deste app e tools/setup.py acima de {1}.",
        ["{0} did not answer within three minutes, so it was stopped."] =
            "{0} não respondeu em três minutos, então foi interrompido.",
        ["{0} was still going after {1:0} minutes, so it was stopped."] =
            "{0} ainda estava rodando depois de {1:0} minutos, então foi interrompido.",
        ["the engine exited {0}"] = "o motor terminou com o código {0}",
        ["the engine wrote nothing"] = "o motor não escreveu nada",
        ["could not read what the engine wrote: "] = "não foi possível ler o que o motor escreveu: ",
        ["none of these"] = "nenhuma destas",
        ["question {0}"] = "pergunta {0}",
        ["question {0} of {1}"] = "pergunta {0} de {1}",
        ["ready"] = "pronto",
        ["needs formatting"] = "precisa formatar",

        // ---- main window --------------------------------------------------
        ["Hackintosh EFI Builder"] = "Hackintosh EFI Builder",
        ["EFI Builder"] = "EFI Builder",
        ["Machine"] = "Máquina",
        ["Builder"] = "Construtor",
        ["Report"] = "Relatório",
        ["Recovery"] = "Recovery",
        ["Installer"] = "Instalador",
        ["USB stick"] = "Pendrive",
        ["Compatible Hardware"] = "Hardware compatível",
        ["Kexts"] = "Kexts",
        ["About"] = "Sobre",
        ["OpenCore, version unread"] = "OpenCore, versão não lida",
        ["{0} configs\n{1} kexts vendored\n"] = "{0} configs\n{1} kexts incluídos\n",
        ["no network to build"] = "gera sem internet",

        // ---- about --------------------------------------------------------
        ["ABOUT"] = "SOBRE",
        ["An OpenCore EFI builder that answers from tables, and says where each table came from."] =
            "Um construtor de EFI do OpenCore que responde a partir de tabelas e diz de onde veio cada tabela.",
        ["PROGRAMS THAT TRAVEL WITH IT"] = "PROGRAMAS QUE VÊM JUNTO",
        ["Not kexts - whole programs, vendored and driven. Each is pinned by hash and carries the licence its project states."] =
            "Não são kexts: são programas inteiros, incluídos e controlados por este. Cada um é fixado por hash e traz a licença que o próprio projeto declara.",
        ["WHERE THE ANSWERS COME FROM"] = "DE ONDE VÊM AS RESPOSTAS",
        ["no upstream recorded"] = "sem origem registrada",
        ["unread"] = "não lida",
        ["OPENCORE"] = "OPENCORE",
        ["unknown"] = "desconhecido",
        ["CONFIGS"] = "CONFIGS",
        ["KEXTS"] = "KEXTS",
        ["SOURCES"] = "FONTES",
        ["NETWORK"] = "INTERNET",
        ["never"] = "nunca",
        ["when asked"] = "quando pedido",
        ["Nothing here reaches the network while it runs. The machine an EFI is prepared on is usually the machine about to be replaced, and it is often not online - so {0} kexts, {1} configs and {2} whole programs travel inside it. The tables below were fetched once, by the tool named beside each, and committed."] =
            "Nada aqui acessa a internet enquanto roda. A máquina onde a EFI é preparada costuma ser a que está para ser substituída, e muitas vezes ela não está online. Por isso {0} kexts, {1} configs e {2} programas inteiros vêm dentro dele. As tabelas abaixo foram baixadas uma vez, pela ferramenta indicada ao lado de cada uma, e salvas no repositório.",
        [" The one thing that does open a connection is {0}."] = " A única coisa que abre uma conexão é {0}.",
        ["Derived means it was read out of the thing itself - a kext's own matching rules, the profile tree. Quoted means a sentence from a document. Reported means somebody ran it and said what happened. None means this repository has no source for it and says so rather than guessing."] =
            "Derivado quer dizer que foi lido da própria coisa: as regras de correspondência do kext, a árvore de perfis. Citado quer dizer uma frase de um documento. Relatado quer dizer que alguém rodou e contou o que aconteceu. Nenhuma quer dizer que este repositório não tem fonte para aquilo e diz isso em vez de chutar.",
        ["derived"] = "derivado",
        ["measured"] = "medido",
        ["quoted"] = "citado",
        ["reported"] = "relatado",
        ["none"] = "nenhuma",

        // ---- builder ------------------------------------------------------
        ["BUILD AN EFI"] = "GERAR UMA EFI",
        ["The same questions the console asks, in the same order. Nothing is answered for you: where this machine can tell us something it is shown as detected, and you still choose."] =
            "As mesmas perguntas do terminal, na mesma ordem. Nada é respondido por você: quando esta máquina consegue informar algo, aparece como detectado, e mesmo assim quem escolhe é você.",
        ["WRITE TO"] = "SALVAR EM",
        ["Change…"] = "Alterar…",
        ["a path, or leave empty to decline"] = "um caminho, ou deixe vazio para recusar",
        ["Stop"] = "Parar",
        ["Continue"] = "Continuar",
        ["Ready"] = "Pronto",
        ["This builds for the machine it runs on."] = "Gera para a máquina em que está rodando.",
        ["Show the EFI folder"] = "Mostrar a pasta EFI",
        ["Start"] = "Começar",
        ["Where should the EFI go?"] = "Onde a EFI deve ser salva?",
        ["That folder has no path this can write to."] = "Essa pasta não tem um caminho onde dê para escrever.",
        ["No engine"] = "Motor não encontrado",
        ["the engine stopped talking: "] = "o motor parou de responder: ",
        ["Stopped"] = "Parado",
        ["Nothing was written. Starting again asks from the top."] =
            "Nada foi salvo. Começar de novo refaz as perguntas desde o início.",
        ["detected"] = "detectado",
        ["Pick one of these first."] = "Escolha uma destas primeiro.",
        ["Build again"] = "Gerar de novo",
        ["Written"] = "Salvo",
        ["The EFI folder is at {0}. Copy it to the EFI partition of your USB drive."] =
            "A pasta EFI está em {0}. Copie-a para a partição EFI do seu pendrive.",
        ["Finished"] = "Concluído",
        ["It ended without writing an EFI. The transcript says why."] =
            "Terminou sem gerar uma EFI. O registro acima explica o motivo.",
        ["Stopped with an error"] = "Parou com um erro",
        ["The engine exited {0}. The transcript says why."] =
            "O motor terminou com o código {0}. O registro acima explica o motivo.",

        // ---- compatible hardware -----------------------------------------
        ["EVERY DEVICE THIS PROGRAM KNOWS"] = "TODOS OS DISPOSITIVOS QUE ESTE PROGRAMA CONHECE",
        ["Search a name, an id or a kext"] = "Busque por nome, id ou kext",
        ["CATEGORY"] = "CATEGORIA",
        ["DEVICE"] = "DISPOSITIVO",
        ["SUPPORT"] = "SUPORTE",
        ["MACOS"] = "MACOS",
        ["VENDOR"] = "FABRICANTE",
        ["ID / DRIVER"] = "ID / DRIVER",
        ["All"] = "Todos",
        ["{0} devices across {1} categories, read out of the same tables a build reads. A device being here means something in this repository claims it - not that every machine it sits in will work."] =
            "{0} dispositivos em {1} categorias, lidos das mesmas tabelas que a geração usa. Um dispositivo estar aqui quer dizer que algo neste repositório dá suporte a ele, não que toda máquina que o tenha vai funcionar.",
        ["{0} devices"] = "{0} dispositivos",
        ["{0} of {1} devices"] = "{0} de {1} dispositivos",
        ["supported"] = "suportado",
        ["unsupported"] = "sem suporte",
        ["untested"] = "não testado",
        ["spoofed"] = "com spoof",
        ["dropped"] = "removido",
        ["Ethernet"] = "Ethernet",
        ["Wi-Fi"] = "Wi-Fi",
        ["Bluetooth"] = "Bluetooth",
        ["Trackpad"] = "Trackpad",
        ["Graphics"] = "Vídeo",
        ["Audio"] = "Áudio",
        ["Card reader"] = "Leitor de cartão",
        ["Mac"] = "Mac",
        ["CPU"] = "CPU",
        ["Storage"] = "Disco",
        ["Camera"] = "Câmera",

        // ---- installer image ---------------------------------------------
        ["INSTALLER IMAGE"] = "IMAGEM DO INSTALADOR",
        ["Turn an installer app into a whole bootable image, in one run."] =
            "Transforma um app instalador em uma imagem inicializável completa, de uma vez só.",
        ["Apple's installer, the EFI folder and legacy BIOS boot, on one image sized to fit. What comes out is a flat sector image - balenaEtcher writes it to a stick from Windows, Linux or macOS, so the stick can be made again later on a machine with no macOS on it."] =
            "O instalador da Apple, a pasta EFI e a inicialização por BIOS legado, numa imagem do tamanho certo. O resultado é uma imagem de setores: o balenaEtcher grava ela num pendrive pelo Windows, Linux ou macOS, então dá para refazer o pendrive depois numa máquina sem macOS.",
        ["This one needs a Mac"] = "Esta parte precisa de um Mac",
        ["THE INSTALLER APP"] = "O APP INSTALADOR",
        ["/Applications/Install macOS Tahoe.app"] = "/Applications/Install macOS Tahoe.app",
        ["Choose…"] = "Escolher…",
        ["Install macOS ….app, from the App Store, softwareupdate, or Mist. Choose… asks for the folder it is in - macOS will not let a panel confirm an app bundle - so you can also drag the app onto this pane, or type its path."] =
            "Install macOS ….app, da App Store, do softwareupdate ou do Mist. Escolher… pede a pasta onde ele está, porque o macOS não deixa uma janela confirmar um app. Você também pode arrastar o app para esta tela ou digitar o caminho dele.",
        ["WHICH ONE"] = "QUAL DELES",
        ["THE EFI FOLDER"] = "A PASTA EFI",
        ["none chosen - the image will carry the installer only"] = "nenhuma escolhida: a imagem vai levar só o instalador",
        ["WRITE THE IMAGE TO"] = "SALVAR A IMAGEM EM",
        ["none chosen"] = "nenhum escolhido",
        ["Make it bootable on a legacy BIOS machine too"] = "Fazer inicializar também em máquinas com BIOS legado",
        ["OpenCore's own DuetPkg, from the version this program carries. A UEFI machine does not need it and is not harmed by it."] =
            "O DuetPkg do próprio OpenCore, da versão que este programa traz. Uma máquina UEFI não precisa dele e não é prejudicada por ele.",
        ["macOS will ask for your administrator password"] = "O macOS vai pedir a sua senha de administrador",
        ["Two things here cannot be done without it: createinstallmedia blesses a volume, and BootInstall writes a master boot record. Press Show what will run to read the exact script before you approve it - it is the same text either way."] =
            "Duas coisas aqui não podem ser feitas sem ela: o createinstallmedia marca um volume como inicializável e o BootInstall grava um registro mestre de inicialização. Clique em Mostrar o que vai rodar para ler o script exato antes de aprovar. É o mesmo texto nos dois casos.",
        ["Show what will run"] = "Mostrar o que vai rodar",
        ["Build the image"] = "Gerar a imagem",
        ["Apple's createinstallmedia is the thing that writes an installer, it ships inside the installer app, and it runs on macOS only. Everything else in this program works here - build the EFI, fetch the recovery, write the stick."] =
            "Quem grava o instalador é o createinstallmedia da Apple, que vem dentro do app instalador e só roda no macOS. Todo o resto deste programa funciona aqui: gerar a EFI, baixar o recovery e gravar o pendrive.",
        ["Which folder is the installer in? Applications, say"] = "Em qual pasta está o instalador? Applications, por exemplo",
        ["That could not be read as a path"] = "Isso não pôde ser lido como um caminho",
        ["macOS handed back {0} with no usable location. Drag the app onto this pane, or type its path above."] =
            "O macOS devolveu {0} sem um local utilizável. Arraste o app para esta tela ou digite o caminho dele acima.",
        ["No installer app in there"] = "Nenhum app instalador aí",
        ["{0} holds no Install macOS ….app. The app is usually in /Applications, or wherever Mist or softwareupdate left it. You can also drag it onto this pane."] =
            "{0} não tem nenhum Install macOS ….app. O app costuma ficar em /Applications ou onde o Mist ou o softwareupdate o deixou. Você também pode arrastá-lo para esta tela.",
        ["{0} installers in that folder"] = "{0} instaladores nessa pasta",
        ["Pick the one to build from."] = "Escolha qual usar.",
        ["The engine's answer could not be read"] = "Não deu para ler a resposta do motor",
        ["That is not an installer app"] = "Isso não é um app instalador",
        ["the app is {0}\ncreateinstallmedia wants about {1} more\nso the image will be {2} GiB"] =
            "o app tem {0}\no createinstallmedia precisa de mais uns {1}\nentão a imagem vai ter {2} GiB",
        ["Which EFI folder?"] = "Qual pasta EFI?",
        ["Where should the image go?"] = "Onde a imagem deve ser salva?",
        ["Choose an installer app first."] = "Escolha um app instalador primeiro.",
        ["Building the image…"] = "Gerando a imagem…",
        ["The image was not built"] = "A imagem não foi gerada",
        ["{0} is ready"] = "{0} está pronto",
        ["It is a flat sector image, so balenaEtcher writes it to a stick from Windows, Linux or macOS. The stick has to be at least as big as the image - which is more gigabytes than the number here, because a stick is sold in decimal GB and this is GiB."] =
            "É uma imagem de setores, então o balenaEtcher grava ela num pendrive pelo Windows, Linux ou macOS. O pendrive precisa ser pelo menos do tamanho da imagem, o que dá mais gigabytes do que o número aqui, porque pendrives são vendidos em GB decimais e este número está em GiB.",

        // ---- kexts --------------------------------------------------------
        ["WHAT IS VENDORED HERE"] = "O QUE VEM INCLUÍDO AQUI",
        ["KEXT"] = "KEXT",
        ["DRIVES"] = "CONTROLA",
        ["VERSION"] = "VERSÃO",
        ["LICENCE"] = "LICENÇA",
        ["not matched by device id"] = "não é ligado por id de dispositivo",
        ["1 device id"] = "1 id de dispositivo",
        ["{0} device ids"] = "{0} ids de dispositivo",
        ["{0} kexts travel inside this program, so a build never reaches the network. {1} of them claim {2} device ids between them, read out of the kexts themselves rather than from a list somebody kept."] =
            "{0} kexts vêm dentro deste programa, então gerar uma EFI nunca acessa a internet. {1} deles atendem {2} ids de dispositivo no total, lidos dos próprios kexts e não de uma lista mantida por alguém.",

        // ---- machine ------------------------------------------------------
        ["NO MACHINE TO SHOW"] = "NENHUMA MÁQUINA PARA MOSTRAR",
        ["READ FROM THIS MACHINE"] = "LIDO DESTA MÁQUINA",
        ["READ FROM "] = "LIDO DE ",
        ["MACOS THIS MACHINE CAN RUN"] = "MACOS QUE ESTA MÁQUINA PODE RODAR",
        ["WHAT SETS THE LIMITS"] = "O QUE DEFINE OS LIMITES",
        ["HARDWARE"] = "HARDWARE",
        ["PART"] = "PEÇA",
        ["DRIVER"] = "DRIVER",
        ["DEVICE ID"] = "ID",
        ["Verdicts come from the same tables the console prints."] =
            "Os resultados vêm das mesmas tabelas que o terminal mostra.",
        ["\"unknown\" means nothing here claims the device - not that it fails."] =
            "\"desconhecido\" quer dizer que nada aqui dá suporte ao dispositivo, não que ele falhe.",
        ["This went wrong: "] = "Algo deu errado: ",
        ["READING THIS MACHINE"] = "LENDO ESTA MÁQUINA",
        ["Asking the system what it has. On Windows this takes a few tens of seconds the first time, because the hardware queries are slow."] =
            "Perguntando ao sistema o que ele tem. No Windows isso leva algumas dezenas de segundos na primeira vez, porque as consultas de hardware são lentas.",
        ["THIS IS A MAC"] = "ISTO É UM MAC",
        ["A Mac"] = "Um Mac",
        ["{0}, so the question is not which kext would claim each device - none of them would - but which driver macOS has given it. {1} of these were read from the running system, along with {2} device ids. A Mac needs no EFI from this program: take a Report on the machine you are converting, or open the Builder with its report."] =
            "{0}, então a pergunta não é qual kext atenderia cada dispositivo (nenhum atenderia), e sim qual driver o macOS deu a ele. {1} destes foram lidos do sistema em execução, junto com {2} ids de dispositivo. Um Mac não precisa de EFI deste programa: tire um Relatório na máquina que você vai converter ou abra o Construtor com o relatório dela.",
        ["Nothing on this machine could be read."] = "Nada nesta máquina pôde ser lido.",
        ["Unnamed machine"] = "Máquina sem nome",
        ["generation"] = "geração",
        ["cores"] = "núcleos",
        ["form factor"] = "formato",
        ["board"] = "placa",
        ["desktop"] = "desktop",
        ["laptop"] = "notebook",
        ["driven by macOS"] = "controlado pelo macOS",
        ["not supported"] = "sem suporte",
        ["not present"] = "ausente",
        // the tally under the machine's name counts, so it is plural there
        ["supported (count)"] = "suportados",
        ["driven by macOS (count)"] = "controlados pelo macOS",
        ["not supported (count)"] = "sem suporte",
        ["unknown (count)"] = "desconhecidos",
        ["not present (count)"] = "ausentes",
        ["Whatever Apple is serving now"] = "O que a Apple estiver oferecendo agora",
        ["Up to {0}"] = "Até {0}",
        ["{0} is one of the boards Apple keeps current, so this Mac is offered the newest macOS there is."] =
            "{0} é uma das placas que a Apple mantém atualizadas, então este Mac recebe o macOS mais novo que existir.",
        ["{0} is offered up to {1}. There is no floor here: nothing this reads knows the oldest macOS a Mac runs."] =
            "{0} recebe até o {1}. Não há limite mínimo aqui: nada do que é lido sabe qual o macOS mais antigo que um Mac roda.",
        ["Apple, for "] = "Apple, para ",
        ["Apple still updates it on"] = "A Apple ainda atualiza em",
        ["Not in Apple's list"] = "Fora da lista da Apple",
        ["{0} is not in any macOS line Apple still serves, which happens to a Mac too old for all of them."] =
            "{0} não está em nenhuma versão do macOS que a Apple ainda oferece, o que acontece com um Mac antigo demais para todas elas.",
        ["{0} and newer"] = "{0} e mais novos",
        ["floor set by {0}; ceiling by {1}"] = "mínimo definido por {0}; máximo por {1}",
        ["floor set by {0}. No part here sets a ceiling - the SMBIOS a build picks has one of its own."] =
            "mínimo definido por {0}. Nenhuma peça aqui define um máximo: o SMBIOS escolhido na geração tem o seu próprio.",
        ["Not bounded here"] = "Sem limites aqui",
        ["Nothing on this machine narrows the range, which is not the same as saying every release works."] =
            "Nada nesta máquina restringe a faixa, o que não é o mesmo que dizer que toda versão funciona.",
        ["{0} from macOS {1}"] = "{0} a partir do macOS {1}",
        [" to {0}"] = " até {0}",
        ["Past that: OpenCore Legacy Patcher restores {0}. Those patches go on an installed macOS, not in the EFI this builds, and OCLP is written for real Macs."] =
            "Além disso: o OpenCore Legacy Patcher restaura {0}. Esses patches são aplicados num macOS já instalado, não na EFI gerada aqui, e o OCLP é feito para Macs de verdade.",
        ["licence unread"] = "licença não lida",
        ["not shipped here"] = "não incluído aqui",
        ["any"] = "qualquer",
        ["current"] = "atual",

        // ---- recovery -----------------------------------------------------
        ["RECOVERY INSTALLER"] = "INSTALADOR RECOVERY",
        ["Put Apple's own installer on the stick, beside the EFI."] =
            "Coloque o instalador da própria Apple no pendrive, ao lado da EFI.",
        ["A whole macOS image is larger than 4 GB and will not fit on the FAT32 partition an EFI lives on. Recovery is about 700 MB: it boots, connects, and downloads the rest of macOS itself. Everything else here works offline - this is the one thing that does not, and it only runs when you press the button."] =
            "Uma imagem completa do macOS tem mais de 4 GB e não cabe na partição FAT32 onde fica a EFI. O Recovery tem uns 700 MB: ele inicia, se conecta e baixa o resto do macOS sozinho. Todo o resto aqui funciona offline. Esta é a única parte que não, e ela só roda quando você clica no botão.",
        ["WHICH MACOS"] = "QUAL MACOS",
        ["Check with Apple"] = "Consultar a Apple",
        ["ONTO"] = "EM",
        ["Download it"] = "Baixar",
        ["Show the folder"] = "Mostrar a pasta",
        ["The drive, not the EFI folder: OpenCore looks for {0} next to EFI, at the root of the partition."] =
            "O disco, não a pasta EFI: o OpenCore procura {0} ao lado da EFI, na raiz da partição.",
        ["no macrecovery is vendored, so there is nothing to drive"] = "o macrecovery não está incluído, então não há o que rodar",
        ["{0} of them, read from macrecovery's own boards.json, which records the newest macOS Apple offers each board. The board is what the request is made with."] =
            "{0} no total, lidos do boards.json do próprio macrecovery, que registra o macOS mais novo que a Apple oferece para cada placa. O pedido é feito com a placa.",
        ["This machine can download during the install"] = "Esta máquina consegue baixar durante a instalação",
        ["Use an Ethernet cable for the install"] = "Use um cabo de rede na instalação",
        ["Recovery cannot finish on this machine"] = "O Recovery não consegue terminar nesta máquina",
        ["Not known for this machine"] = "Desconhecido para esta máquina",
        ["asking Apple…"] = "consultando a Apple…",
        ["Apple did not answer"] = "A Apple não respondeu",
        ["Apple is serving {0} {1} today. The row still asks for whatever is newest when you press download, not for this number."] =
            "A Apple está oferecendo o {0} {1} hoje. A linha continua pedindo o mais novo no momento em que você clicar em baixar, e não este número.",
        ["Which drive? Pick the root of it, not the EFI folder."] = "Qual disco? Escolha a raiz dele, não a pasta EFI.",
        ["Fetching {0} from Apple…"] = "Baixando {0} da Apple…",
        ["connecting…"] = "conectando…",
        ["{0} left"] = "faltam {0}",
        ["Nothing was fetched"] = "Nada foi baixado",
        ["{0} is on the stick"] = "{0} está no pendrive",
        ["It sits in {0} at the root of {1}. OpenCore lists it at the boot menu. The rest of macOS comes down during the install, so that machine needs Ethernet or a card macOS already drives."] =
            "Ele fica em {0}, na raiz de {1}. O OpenCore mostra ele no menu de inicialização. O resto do macOS é baixado durante a instalação, então aquela máquina precisa de cabo de rede ou de uma placa que o macOS já reconheça.",
        ["almost done"] = "quase pronto",

        // ---- report -------------------------------------------------------
        ["TAKE A REPORT"] = "TIRAR UM RELATÓRIO",
        ["Read this machine, and write what was read to a file."] =
            "Lê esta máquina e salva o que foi lido num arquivo.",
        ["A USB stick is usually made on a computer that already works, not on the one being converted. Run this there, carry the file back, and the builder can answer for that machine instead of this one - graphics, audio, network and the trackpad included."] =
            "O pendrive costuma ser feito num computador que já funciona, não no que vai ser convertido. Rode isto lá, traga o arquivo de volta e o construtor responde por aquela máquina em vez desta, incluindo vídeo, áudio, rede e trackpad.",
        ["The machine's ACPI tables are dumped beside it where that is possible, because the SSDTs have to be written against the tables of the machine they are for."] =
            "As tabelas ACPI da máquina são salvas ao lado dele quando possível, porque os SSDTs precisam ser escritos a partir das tabelas da máquina a que se destinam.",
        ["Take the report"] = "Tirar o relatório",
        ["Show the file"] = "Mostrar o arquivo",
        ["Where should the report go?"] = "Onde o relatório deve ser salvo?",
        ["Reading this machine…"] = "Lendo esta máquina…",
        ["Nothing was written"] = "Nada foi salvo",
        ["Copy {0} to the machine you build on, open the Builder there, and answer “{1}”."] =
            "Copie {0} para a máquina onde você vai gerar a EFI, abra o Construtor lá e responda “{1}”.",
        ["Another machine, and I have its hardware report"] = "Outra máquina, e eu tenho o relatório de hardware dela",

        // ---- USB stick ----------------------------------------------------
        ["THE USB STICK"] = "O PENDRIVE",
        ["Put the EFI and the installer on it."] = "Coloque a EFI e o instalador nele.",
        ["Both folders go at the root of the stick, side by side - the recovery does not go inside the EFI folder, because OpenCore looks for it beside itself. Only removable disks are listed here, and never the one this computer booted from."] =
            "As duas pastas ficam na raiz do pendrive, lado a lado. O recovery não vai dentro da pasta EFI, porque o OpenCore procura ele ao seu lado. Só discos removíveis aparecem aqui, e nunca o disco de onde este computador iniciou.",
        ["WHICH STICK"] = "QUAL PENDRIVE",
        ["Look again"] = "Procurar de novo",
        ["EFI"] = "EFI",
        ["INSTALLER"] = "INSTALADOR",
        ["Copy onto the stick"] = "Copiar para o pendrive",
        ["Show the stick"] = "Mostrar o pendrive",
        ["type the disk name to confirm"] = "digite o nome do disco para confirmar",
        ["Erase it"] = "Apagar",
        ["that is not {0}"] = "isso não é {0}",
        ["Looking…"] = "Procurando…",
        ["Nothing here could ask: {0}. That is not the same as no stick being plugged in."] =
            "Não foi possível consultar: {0}. Isso não é o mesmo que não ter pendrive conectado.",
        ["No removable disk is plugged in. This only ever lists removable, external, physical disks, and never the one this computer booted from{0}."] =
            "Nenhum disco removível conectado. Aqui só aparecem discos físicos, externos e removíveis, e nunca o disco de onde este computador iniciou{0}.",
        ["One, and it is not the disk this computer booted from."] =
            "Um, e não é o disco de onde este computador iniciou.",
        ["{0} of them. The disk this computer booted from is not among them and cannot be."] =
            "{0} no total. O disco de onde este computador iniciou não está entre eles e nunca vai estar.",
        ["Ready. Writes to {0}"] = "Pronto. Grava em {0}",
        ["This one has to be formatted first"] = "Este precisa ser formatado primeiro",
        ["This erases everything on {0}, {1} ({2})"] = "Isto apaga tudo em {0}, {1} ({2})",
        [", mounted at {0}."] = ", montado em {0}.",
        [" There is no undoing it."] = " Não tem como desfazer.",
        ["It becomes one FAT32 partition under GPT, which is what OpenCore boots from. Type {0} below to turn the button on."] =
            "Ele vira uma única partição FAT32 em GPT, que é de onde o OpenCore inicia. Digite {0} abaixo para liberar o botão.",
        ["This system cannot do it from here - it needs a root or administrator the engine does not have. Press it anyway and the exact commands to run yourself are printed below."] =
            "Este sistema não consegue fazer isso daqui: precisa de permissão de root ou administrador que o motor não tem. Clique mesmo assim e os comandos exatos para você rodar aparecem abaixo.",
        ["type {0}"] = "digite {0}",
        ["Which folder holds {0}?"] = "Qual pasta contém {0}?",
        ["That stick is not mounted"] = "Esse pendrive não está montado",
        ["{0} has no mounted volume, so there is nowhere to copy to. Format it first, or mount it."] =
            "{0} não tem volume montado, então não há para onde copiar. Formate ou monte ele primeiro.",
        ["Copying onto {0}…"] = "Copiando para {0}…",
        ["Nothing was copied"] = "Nada foi copiado",
        ["Boot the machine from it. OpenCore's picker lists macOS Base System if the installer is on there; the rest of macOS comes down during the install, so that machine needs Ethernet or a card macOS drives."] =
            "Inicie a máquina por ele. O menu do OpenCore mostra macOS Base System se o instalador estiver lá. O resto do macOS é baixado durante a instalação, então aquela máquina precisa de cabo de rede ou de uma placa que o macOS reconheça.",
        ["Erasing {0}…"] = "Apagando {0}…",
        ["It was not erased"] = "Não foi apagado",
        ["{0} is formatted"] = "{0} está formatado",
        ["Now copy the EFI and the installer onto it."] = "Agora copie a EFI e o instalador para ele.",
    };
}
