---
title: O app
---

# O app

Está tudo num download só. Pegue o pacote do seu sistema em
[Releases](https://github.com/yusufklncc/Hackintosh-for-All-Computers/releases),
descompacte e rode.

=== "Windows"

    `HackintoshEFIBuilder-win-x64.zip`

    Descompacte em qualquer lugar e rode `HackintoshEFIBuilder.exe`.

=== "macOS"

    `HackintoshEFIBuilder-osx-arm64.zip` para Apple silicon,
    `HackintoshEFIBuilder-osx-x64.zip` para Intel.

    Descompacte, arraste `HackintoshEFIBuilder.app` para a pasta Aplicativos
    e abra a partir dali.

=== "Linux"

    `HackintoshEFIBuilder-linux-x64.AppImage`

    ```
    chmod +x HackintoshEFIBuilder-linux-x64.AppImage
    ./HackintoshEFIBuilder-linux-x64.AppImage
    ```

    Ou `HackintoshEFIBuilder-linux-x64.zip`, descompactado e rodado.

Sem .NET, sem Python, sem nenhum tipo de runtime. Cada pacote traz dois
programas: `HackintoshEFIBuilder`, a janela, e `EFIBuilderEngine`, o construtor
que ela roda. Mantenha os dois juntos.

A janela não reimplementa nada do construtor. Ela roda o mesmo programa que o
terminal roda e desenha as respostas dele, então uma tela aqui não tem como
dizer algo que o terminal não diria.

!!! note "Em português"
    O app aparece em português quando o idioma do seu sistema é português, e em
    inglês nos outros casos. Para escolher na mão, defina a variável de ambiente
    `HFAC_LANG` como `pt` ou `en` antes de abrir. As perguntas do construtor
    seguem o mesmo idioma da janela.

!!! warning "A primeira execução é recusada, no Windows e no macOS"
    Nenhum dos programas é assinado por uma empresa que pague a Microsoft ou a
    Apple. Isso dá uma janela de aviso em cada sistema, e [Se o seu sistema
    bloquear](blocked.md) tem os passos.

## As nove telas

### Máquina

Onde ele abre: o nome do modelo, o que é cada peça, se o macOS a reconhece,
qual kext faz isso e o macOS mais antigo que este hardware consegue iniciar,
junto com a peça que define esse mínimo.

`desconhecido` quer dizer que nenhuma tabela aqui dá suporte ao dispositivo, e
não que ele falhe.

![A tela Máquina](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/App/machine.png)

### Construtor

Faz as perguntas e gera a pasta EFI. Ele não responde nenhuma por você: quando a
máquina consegue informar algo, a opção aparece marcada como *detectado*, e
mesmo assim quem escolhe é você.

[Gere a sua EFI :material-arrow-right:](efi.md){ .md-button }

![A tela Construtor](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/App/builder.png)

### Relatório

Lê esta máquina para um único arquivo JSON e extrai as tabelas ACPI dela ao
lado. É esse o arquivo a levar para o computador onde você vai gerar a EFI,
quando o pendrive estiver sendo preparado em outro lugar.

Ele não guarda nenhum número de série nem uma lista bruta de dispositivos, então
é seguro mandar para alguém que esteja te ajudando.

[Gerar para outra máquina :material-arrow-right:](another-machine.md){ .md-button }

![A tela Relatório](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/App/report.png)

### Recovery

Coloca o instalador da própria Apple no pendrive, ao lado da EFI: uns 700 MB
que iniciam, se conectam e baixam o resto do macOS sozinhos. É a solução quando
uma imagem completa não cabe: a partição FAT32 onde fica a EFI não aceita um
arquivo com mais de 4 GB.

Cada versão que a tabela de placas oferece é um quadro, da mais nova para a mais
antiga. O primeiro pede o macOS que a Apple estiver oferecendo, e não um número
de versão; a tabela de placas não diz qual é, então o nome ao lado vem do
`data/mac.toml`, e **Consultar a Apple** pergunta direto à Apple a resposta de
hoje.

Antes de você baixar qualquer coisa, ele diz se a máquina para a qual você está
gerando consegue mesmo terminar: o recovery baixa o macOS *naquela máquina*,
então um notebook cuja única placa é um Wi-Fi Realtek inicia o instalador e
para. Se a Ethernet dela for reconhecida, ele avisa para usar um cabo. Veja
[Prepare o pendrive](usb.md).

![A tela Recovery](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/App/recovery.png)

### Instalador

Transforma um app instalador numa imagem inicializável completa, de uma vez só:
calcula o tamanho, particiona, chama o `createinstallmedia` da Apple, faz a
imagem iniciar também em máquinas com BIOS legado usando o DuetPkg do próprio
OpenCore e copia a pasta EFI para dentro.

O resultado é uma imagem de setores, então o balenaEtcher grava ela num pendrive
a partir de qualquer sistema: o pendrive pode ser refeito depois numa máquina
sem macOS.

Só no macOS, porque o `createinstallmedia` é um programa da Apple que vem dentro
do app; no Windows e no Linux a tela avisa isso. É o único lugar do programa que
pede senha de administrador, e ele mostra o script que vai rodar antes de pedir.

[Preparar o pendrive num Mac :material-arrow-right:](mac-installer.md){ .md-button }

### Pendrive

Encontra os discos removíveis, formata um se você quiser e copia as duas pastas
para ele nos lugares certos. Ele diz se o pendrive pode ser gravado do jeito que
está (FAT32 em GPT com espaço livre) ou se precisa ser apagado antes.

Ele lista só discos removíveis, nunca o disco de onde o computador iniciou, e
para apagar ele pede que você digite o nome do disco antes de começar.

![A tela Pendrive](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/App/usb.png)

### Hardware compatível

Lista 766 dispositivos em 8 categorias, tudo o que este repositório conhece,
com busca por nome, id ou kext e filtros por categoria, fabricante e suporte.
É lido das mesmas tabelas que a geração usa, então não tem como divergir do que
o construtor faria.

![A tela Hardware compatível](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/App/hardware.png)

### Kexts

Lista os 42 kexts que vêm dentro do programa, com o projeto de onde cada um vem,
a versão, a licença e quantos ids de dispositivo ele atende, lidos dos próprios
kexts e não de uma lista mantida por alguém.

![A tela Kexts](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/App/kexts.png)

### Sobre

Diz de onde vem cada resposta: qual ferramenta baixou cada tabela, se ela foi
derivada, medida, citada ou relatada, e as áreas que não têm fonte nenhuma, ditas
claramente em vez de chutadas.

![A tela Sobre](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/App/about.png)
