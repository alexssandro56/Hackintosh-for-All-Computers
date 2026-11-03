---
title: Preparar o pendrive num Mac
---

# Preparar o pendrive num Mac

Se você já tem um Mac funcionando, consegue fazer algo que os outros caminhos
deste site não fazem: **um pendrive só, com um instalador offline completo, a
EFI e inicialização em BIOS legado**, montado antes dentro de uma imagem de
disco, para poder ser clonado em quantos pendrives você quiser sem refazer nada.

Este é o caminho longo. Vale a pena quando:

- a máquina onde você vai instalar [não tem uma rede que o macOS consiga
  usar](usb.md), então o [recovery](usb.md#com-recovery-o-programa-faz-tudo) não
  consegue terminar;
- **e** ela é uma máquina com BIOS legado, ou você quer que o mesmo pendrive
  funcione numa;
- **e** você prefere o instalador da própria Apple a uma
  [imagem pronta](images.md) que outra pessoa preparou.

!!! tip "O programa faz tudo isso por você"
    Abra a tela **Instalador**, aponte para o app do instalador, e ela roda
    todos os passos desta página de uma vez: calcula o tamanho da imagem,
    particiona, chama o `createinstallmedia`, faz ela iniciar numa máquina com
    BIOS, copia a pasta EFI e te entrega a imagem.

    O macOS pede a senha de administrador uma vez (dois dos passos não podem
    ser feitos sem ela), e a tela mostra o script exato antes de você aprovar.

    **O resto desta página é esse mesmo trabalho feito à mão**, o que vale a
    leitura se você quer saber o que a tela está fazendo, se prefere rodar a
    parte privilegiada você mesmo (o `--script` mostra ela), ou se algo deu
    errado e você precisa continuar do meio.

!!! info "Você precisa de um Mac para esta página, e só para ela"
    O `createinstallmedia` é um binário da Apple que vem dentro do app do
    instalador e só roda no macOS. Todo o resto que este repositório faz
    funciona no Windows e no Linux: veja [Sem a janela](terminal.md).

## 1. Consiga o instalador

=== "Mist"

    O [**Mist**](https://github.com/ninxsoft/Mist) é o caminho mais fácil, e o
    melhor se você quer uma versão que não está sendo oferecida para este Mac.
    Ele lista todo macOS que a Apple ainda publica, com versão, build, data de
    lançamento **e tamanho**, e depois monta o app do instalador para você.

    ```
    brew install --cask mist
    ```

    Ou pegue o app na
    [página de releases](https://github.com/ninxsoft/Mist/releases). Tem
    licença MIT e roda no Monterey ou mais novo. Existe um
    [`mist-cli`](https://github.com/ninxsoft/mist-cli) se você preferir não
    abrir uma janela.

    Escolha **Generate an Application Bundle (.app)**: é isso que o
    `createinstallmedia` precisa. As outras saídas que ele oferece, `.iso` e
    `.pkg`, são para máquinas virtuais e para distribuição, não para isto.

    Duas coisas que ele faz e que importam num download de 15 GB: confere os
    checksums do chunklist quando termina, e tenta de novo sozinho quando uma
    transferência cai.

    !!! note "Ele pode pedir Acesso Total ao Disco"
        O próprio README dele diz isso, em Ajustes do Sistema → Privacidade e
        Segurança.

    O tamanho que ele lista é a resposta do passo 2 antes de você baixar
    qualquer coisa, e esse é o motivo principal para olhar aqui primeiro.

=== "softwareupdate"

    O macOS consegue baixar os próprios instaladores, sem precisar instalar
    nada antes:

    ```
    softwareupdate --list-full-installers
    softwareupdate --fetch-full-installer --full-installer-version 26.6.2
    ```

    Ele só oferece o que o catálogo da Apple entrega para *este* Mac, então uma
    versão mais antiga pode não estar na lista. Quando está, é o caminho mais
    curto.

De um jeito ou de outro, o instalador vai parar em `/Applications` como
`Install macOS <nome>.app`.

## 2. Calcule o tamanho que o pendrive precisa ter

A página da Apple diz só *"A 32GB flash drive has more than enough storage
space for any macOS installer, and 16GB is enough for most earlier versions"*
(um pendrive de 32GB tem espaço de sobra para qualquer instalador, e 16GB basta
para a maioria das versões anteriores). A segunda metade deixou de ser verdade,
já que só o instalador do Tahoe tem 17 GiB, e nenhuma das duas ajuda a definir o
tamanho de uma imagem de disco. Então meça:

```
du -sh "/Applications/Install macOS Tahoe.app"
17G
```

**Depois some uns 2,5 GiB, e não meio gigabyte.** O `createinstallmedia` não só
copia o app: ele coloca um recovery do lado, então o volume precisa ser bem
maior do que o que vai ser gravado. Medido num instalador do Tahoe 26.6.2:

| | |
|---|---|
| o `du -sh` mostra | 17,00 GiB |
| o volume que o `createinstallmedia` aceitou | **19,15 GiB** |
| então o adicional em relação ao app é | **2,15 GiB** |

!!! danger "Duas unidades, com 7% de diferença entre elas"
    `hdiutil -size 18g` quer dizer 18 **GiB**. O `diskutil` mostra **GB
    decimais**. Então uma imagem pedida como `18g` aparece como `19.3 GB`, e um
    volume que mostra `18.8 GB` tem na verdade 17,5 GiB. O `du -sh` conta em
    GiB, como o `hdiutil`.

    Misturar as duas é como um pendrive acaba faltando um gigabyte depois de
    vinte minutos de cópia. Calcule tudo em GiB e trate o que o `diskutil`
    mostra como outro jeito de dizer o mesmo número.

Some a partição EFI por cima: 500 MB é muito mais do que uma pasta EFI precisa
(uns 7 MB), e é o menor tamanho que deixa espaço para guardar uma ou duas
configs reserva do lado.

Então, para um instalador de 17 GiB: `17 + 2,15 + 0,5` = 19,65, arredondado
para o próximo gigabyte inteiro: **`-size 20g`**. Foi com isso que um pendrive
do Tahoe foi montado de verdade, e ele terminou com uns 0,4 GiB sobrando.

!!! tip "Ou deixe o comando calcular para você"
    Chutar é opcional. Monte a imagem com o tamanho que achar, rode o passo 5,
    e se ele recusar vai dizer exatamente quanto falta:

    ```
    /Volumes/USB is not large enough for install media.
    An additional 1.76 GB is needed.
    ```

    Some isso ao tamanho de volume que o `diskutil list` mostra, arredonde para
    cima e monte de novo. Custa uma tentativa que falha e nenhuma conta, e a
    tentativa é rápida, porque ele confere o tamanho antes de copiar qualquer
    coisa.

## 3. Monte numa imagem de disco, não no pendrive

Fazer o trabalho num `.dmg` primeiro é o que torna isso repetível. Particione,
preencha e depois clone para um pendrive, ou para cinco pendrives, ou para o
mesmo pendrive daqui a um ano quando ele tiver quebrado.

```
hdiutil create -size 20g -type UDIF -layout NONE -o installer
```

O `-layout NONE` importa: ele te dá um dispositivo cru, sem nenhum mapa de
partições, que é o que o próximo passo quer gravar.

Conecte a imagem sem deixar o Finder montar nada:

```
hdiutil attach -nomount installer.dmg
```

Isso mostra o dispositivo que ela virou, por exemplo `/dev/disk4`. **Todos os
comandos abaixo usam esse número, e errar apaga outra coisa.** Confira com o
`diskutil list` antes de digitar em qualquer lugar.

## 4. Particione

```
diskutil partitionDisk /dev/disk4 MBR "MS-DOS FAT32" EFI 500m JHFS+ USB R
```

O que dá:

```
#:                       TYPE NAME                    SIZE       IDENTIFIER
0:     FDisk_partition_scheme                        +21.5 GB    disk4
1:                 DOS_FAT_32 EFI                     500.0 MB   disk4s1
2:                  Apple_HFS USB                     21.0 GB    disk4s2
```

Quatro coisas nesse comando são essenciais:

**`MBR`, e não `GPT`.** Uma máquina com BIOS legado inicia por um master boot
record. Num disco GPT o `BootInstall` ainda funciona, mas a máquina para a qual
você está montando isto é o motivo de você estar nesta página.

**A partição FAT32 vem primeiro.** O `BootInstall` olha para `disk<N>s1` e para
nenhum outro lugar: ele confere se essa partição é `FAT_32` ou `EFI` e para se
não for. Coloque o volume do instalador primeiro e a ferramenta vai recusar um
disco que está organizado perfeitamente.

**`R` no último tamanho.** Quer dizer *o resto*, então não há conta para errar e
nenhum espaço sobra no fim. Escrever `13.55g` também funciona; escrever
`13,55gb` com vírgula não funciona, e as aspas curvas que um editor de texto
coloca em volta de `"MS-DOS FAT32"` também não.

**`JHFS+`, e não APFS.** O `createinstallmedia` apaga o volume que você der para
ele em Mac OS Expandido (Reg. Cronológico) de qualquer jeito (a página da Apple
diz isso), e um contêiner APFS aqui só seria jogado fora.

## 5. Grave o instalador

```
sudo "/Applications/Install macOS Sequoia.app/Contents/Resources/createinstallmedia" \
  --volume /Volumes/USB --nointeraction
```

O `--nointeraction` pula a pergunta *digite Y para apagar*. Deixe sem ele na
primeira vez se você preferir ser perguntado.

```
Erasing disk: 0%... 10%... 20%... 30%... 100%
Copying essential files...
Copying the macOS RecoveryOS...
Making disk bootable...
Copying to disk: 0%... 10%... 20%... 100%
Install media now available at "/Volumes/Install macOS Tahoe"
```

*Copying the macOS RecoveryOS* é a linha que explica o passo 2: o recovery vai
do lado do instalador, e ele é a maior parte dos dois gigabytes que o tamanho do
próprio app não conta.

O volume é apagado, preenchido e renomeado. Menos de um minuto numa imagem de
disco num SSD interno; dez a vinte minutos num pendrive, onde a velocidade de
gravação decide.

!!! failure "Se ele recusar no final"
    *"is not large enough for install media. An additional N is needed"* quer
    dizer que o passo 2 ficou curto exatamente nesse valor. A imagem precisa
    ser montada de novo com o tamanho maior; não dá para aumentar no lugar.
    *"The volume could not be unmounted"* normalmente quer dizer que o Finder
    ou o Spotlight está com ele aberto; feche qualquer janela dele e rode de
    novo.

## 6. Faça a partição EFI iniciar num BIOS legado

Esta é a parte que não tem nada a ver com a Apple. Numa máquina UEFI você pode
pular tudo isto: copie a pasta EFI no passo 7 e pare.

O OpenCore inicia uma máquina com BIOS pelo **DuetPkg**, um ambiente UEFI
carregado a partir do MBR. As peças vêm na versão do OpenCore, não neste
repositório:

1. Baixe `OpenCore-<versão>-RELEASE.zip` de
   [acidanthera/OpenCorePkg](https://github.com/acidanthera/OpenCorePkg/releases)
   e extraia. **Use a mesma versão com que a sua pasta EFI foi gerada**: as
   EFIs deste repositório mostram qual na barra lateral do app.
2. Abra `Utilities/LegacyBoot/`. Ela tem `boot0`, `boot1f32`, `bootX64` e os
   scripts que instalam esses arquivos.
3. Rode, de dentro dessa pasta, e responda com o número do seu disco:

```
cd Utilities/LegacyBoot
sudo ./BootInstall_X64.tool
```

Ele grava o `boot0` no master boot record, ajusta o setor de inicialização da
partição FAT32 com o `boot1f32`, copia o `bootX64` para a partição **como
`boot`** e marca a partição 1 como ativa. As palavras dele mesmo se algo der
errado: *"Disable SIP in the case of any problems with installation!!!"*
(desative o SIP se houver qualquer problema na instalação).

!!! tip "Você não precisa copiar o `boot` à mão"
    A ferramenta faz isso. E não existe `boot6`, `boot7` ou `boot9` aqui: esses
    são arquivos de terceiro estágio do **Clover**, outro bootloader, e não
    fazem nada num pendrive com OpenCore.

    Onde o Clover oferecia variantes numeradas, o OpenCore oferece duas
    versões: `BootInstall_X64.tool` e `BootInstall_X64_BlockIO.tool`. Se a
    máquina chega no menu e depois não consegue ler o disco, a BlockIO é a
    outra coisa para tentar. As variantes `IA32` estão lá para firmwares de 32
    bits.

## 7. Coloque a pasta EFI

Monte a partição FAT32 e copie a pasta `EFI` que o construtor gerou para a raiz
dela, do lado do arquivo `boot` que a ferramenta acabou de deixar lá:

```
/Volumes/EFI/
├── boot            gravado pelo BootInstall, só num pendrive legado
└── EFI/
    ├── BOOT/
    └── OC/
```

O volume do instalador não é tocado por nada disso: o instalador da Apple está
em `disk4s2` e o OpenCore está em `disk4s1`, e nenhum sabe do outro até o menu
de inicialização oferecer os dois.

## 8. Grave num pendrive

Desconecte a imagem primeiro; nada abaixo deve rodar enquanto ela ainda estiver
conectada:

```
hdiutil detach /dev/disk4
```

=== "Por este Mac"

    O `asr` é o caminho nativo e copia o mapa de partições junto, então o
    pendrive sai exatamente como a imagem: MBR, as duas partições, o registro
    de inicialização e tudo.

    ```
    diskutil list                       # ache o pendrive, e confira duas vezes
    sudo asr restore --source installer.dmg --target /dev/disk5 \
      --erase --noprompt
    ```

    **O `--erase` destrói tudo no destino.** Leia o número do dispositivo em
    voz alta antes de apertar enter.

=== "De qualquer lugar, com o balenaEtcher"

    `hdiutil create -type UDIF -layout NONE` grava uma **imagem plana de
    setores**, e não uma imagem de disco empacotada: o arquivo não tem o
    trailer `koly`, começa com a tabela de partições e tem exatamente o tamanho
    pedido. Ele já é o que uma ferramenta de gravação de imagens quer.

    Então renomeie e grave como qualquer outra imagem:

    ```
    mv installer.dmg tahoe-installer.raw
    ```

    Depois abra no [balenaEtcher](https://www.balena.io/etcher/), **no
    Windows, no Linux ou no macOS**, escolha o pendrive e grave. O nome é só
    para o seletor de arquivos do Etcher; `.raw` e `.img` funcionam, e os bytes
    são os mesmos de um jeito ou de outro.

    É isso que faz a imagem de disco valer a pena: o pendrive pode ser feito de
    novo depois, numa máquina que nem tem macOS.

!!! warning "O pendrive precisa ser pelo menos do tamanho da imagem"
    Uma imagem de 20 GiB tem 21,5 GB na unidade em que pendrives são vendidos,
    então um pendrive de *20 GB* é pequeno demais e um de *32 GB* é o próximo
    tamanho que serve. É a mesma diferença entre GiB e GB do passo 2.

Guarde o arquivo. Da próxima vez que precisar deste pendrive, você está a uma
gravação dele, e o `gzip` comprime bastante para guardar; o Etcher lê uma
imagem comprimida tão bem quanto uma sem compressão.

---

Daqui em diante o pendrive funciona como qualquer outro: [configure a
BIOS](bios.md), inicie por ele e [instale o macOS](installation.md).
