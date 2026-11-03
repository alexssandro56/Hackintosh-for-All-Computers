---
title: Primeira inicialização
---

# Primeira inicialização

Escolha o pendrive no menu de inicialização do computador. A tela do OpenCore
aparece; aperte ++enter++ em **Install macOS "Sonoma"**, ou na versão que for a
sua.

Um texto vai começar a correr pela tela. É o modo *verbose*, mostrando o que
acontece enquanto a máquina inicia. Se ele continuar andando, está tudo bem:
depois de um tempo aparecem o logo da Apple e o instalador.

!!! failure "O texto para e não volta a andar"
    Tire uma foto de onde ele parou. As últimas linhas são o que uma issue
    precisa; um `machine.json` da tela **Relatório** junto transforma o palpite
    numa resposta.

## Se aparecer um erro de SMBIOS

![O erro de SMBIOS incompatível](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/change-smbios.png)

Isso é uma incompatibilidade entre o macOS que você está tentando instalar e o
modelo de Mac que a config finge ser. A Apple decide o que vai instalar a partir
desse modelo, e não do seu hardware.

O construtor confere isso antes de gerar qualquer coisa e oferece um modelo que
recebe a versão que você pediu: veja [qual macOS e por que não é só sobre
kexts](efi.md#qual-macos-e-por-que-não-é-só-sobre-kexts). Se você chegou aqui
mesmo assim, abra o `config.plist` num editor de texto, troque o
`SystemProductName` por um modelo para o qual a Apple oferece essa versão e
inicie de novo.

## BIOS legado

Qual arquivo inicia depende de qual bootloader o colocou ali, e as duas
respostas são diferentes. Olhe a raiz da partição EFI.

=== "Uma EFI deste repositório (OpenCore)"

    Há um arquivo só, chamado `boot`, e foi o `BootInstall` que o gravou. Não
    há variantes numeradas para testar: se ele não iniciar, a outra opção que
    existe é a versão **BlockIO** do mesmo arquivo, para firmwares que não
    conseguem ler o disco do jeito normal.

    Pegue `Utilities/LegacyBoot/` na
    [versão do OpenCore](https://github.com/acidanthera/OpenCorePkg/releases)
    correspondente à sua EFI e rode `BootInstall_X64_BlockIO.tool` em vez de
    `BootInstall_X64.tool`. Veja
    [Preparar o pendrive num Mac](mac-installer.md#6-faça-a-partição-efi-iniciar-num-bios-legado),
    que é a mesma tarefa feita pelo macOS.

=== "Uma imagem pronta (Clover)"

    `boot6`, `boot7`, `boot9` e os outros são arquivos de terceiro estágio do
    **Clover**, e um pendrive gravado a partir de uma das [imagens](images.md)
    deste site pode trazê-los. São variantes para controladores de disco
    diferentes, então testar um por um faz sentido de verdade:

    1. Renomeie `boot` para `boot-default`.
    2. Renomeie `boot6` para `boot` e teste.
    3. Depois `boot7`, depois `boot9`.

    Nada disso vale para uma EFI do OpenCore, onde esses arquivos simplesmente
    não existem.

---

Quando o instalador estiver na tela, o kext de Ethernet ou de Wi-Fi é a peça
importante para o que vem a seguir.

[Passos da instalação do macOS :material-arrow-right:](installation.md){ .md-button .md-button--primary }
