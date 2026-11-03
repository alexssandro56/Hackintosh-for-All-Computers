---
title: Prepare o pendrive
---

# Prepare o pendrive

O pendrive precisa de duas coisas: a pasta `EFI` que você acabou de gerar e o
próprio macOS. Há dois jeitos de conseguir o segundo, e eles levam a pendrives
diferentes.

| | De onde vem o macOS | O que custa |
|---|---|---|
| **Recovery** | O programa baixa | Uns 700 MB. Inicia, se conecta e baixa o resto do macOS na máquina que está sendo convertida. Precisa de uma placa de rede que o macOS já reconheça. Qualquer pendrive de 2 GB. |
| **Uma imagem pronta** | Você baixa deste site | Uns 12 GB de `.raw`, gravados com o balenaEtcher. Instala sem internet nenhuma. Pendrive de 16 GB ou mais. |

O recovery é o caminho mais curto e o que o programa consegue fazer do começo ao
fim. Uma imagem é a solução quando a máquina não tem uma rede que o macOS consiga
usar durante a instalação, ou quando a conexão é lenta demais para confiar.

## Com recovery: o programa faz tudo

1. Abra a tela **Recovery**, escolha o macOS que você quer e clique em baixar.

    As linhas abaixo da primeira são versões com nome. **A primeira linha é o
    macOS mais novo**: ela pede à Apple o que estiver sendo oferecido hoje, e
    não um número de versão.

    A tabela de placas que o OpenCore traz registra essas placas como `latest`
    e nunca diz o nome da versão, então o nome ao lado vem do `data/mac.toml`,
    que este repositório atualiza a partir dos dados da própria Apple.
    **Consultar a Apple** pergunta direto à Apple a resposta de hoje.

    Ele salva `BaseSystem.dmg` e `BaseSystem.chunklist` numa pasta
    `com.apple.recovery.boot`.

2. Abra a tela **Pendrive**. Ela lista os discos removíveis que encontra e diz,
   para cada um, se ele está pronto do jeito que está (FAT32 em GPT com espaço
   livre) ou se precisa ser apagado antes. Se precisar, clique em formatar e
   digite o nome do disco quando ele pedir.

3. Clique em copiar. Ele coloca as duas pastas na raiz do pendrive, lado a lado:

```
/Volumes/USB/
├── EFI/                       a pasta que o construtor gerou
└── com.apple.recovery.boot/   BaseSystem.dmg + BaseSystem.chunklist
```

O pendrive é só isso. Nada entra dentro da `EFI` que já não estivesse lá, e a
pasta do recovery também não fica dentro dela: o OpenCore procura esse nome ao
seu lado.

Inicie pelo pendrive e o menu do OpenCore mostra **macOS Base System**. Escolha
essa opção e o instalador baixa o resto do macOS sozinho.

!!! warning "O download acontece na máquina que está sendo convertida"
    Não na que preparou o pendrive. Essa máquina precisa de Ethernet, ou de uma
    placa Wi-Fi que o macOS já reconheça, durante a instalação.

    **A tela Recovery diz em qual caso você está**, antes de você baixar
    qualquer coisa, lendo isso do relatório de hardware:

    | O que ela diz | O que significa |
    |---|---|
    | *Esta máquina consegue baixar durante a instalação* | O Wi-Fi tem driver no macOS. Não precisa fazer mais nada. |
    | *Use um cabo de rede na instalação* | O seu Wi-Fi não tem driver no macOS, mas a sua Ethernet tem. O recovery funciona: conecte um cabo antes de começar. É o caso comum em notebooks com Wi-Fi Realtek. |
    | *O Recovery não consegue terminar nesta máquina* | Nenhuma das placas é reconhecida. Use [uma imagem completa](images.md) ou instale uma placa com suporte. |
    | *Desconhecido para esta máquina* | Não há relatório para ler. Ele não vai chutar. |

## Com uma imagem

1. Pegue um `.raw` em [Imagens do macOS](images.md) e extraia do zip.

2. Baixe o [balenaEtcher](https://www.balena.io/etcher/). Clique em **Flash from
   file** e escolha o `.raw`, clique em **Select target** e escolha o pendrive,
   depois em **Flash!**

    ![Gravando a imagem com o balenaEtcher](https://user-images.githubusercontent.com/78423442/154849816-0a04602a-9064-4780-9d4e-ed86254b4fea.png)

3. Quando terminar, tire o pendrive e conecte de novo. Uma partição `EFI`
   aparece em *Este Computador*.

4. Copie a sua pasta `EFI` para essa partição, substituindo o que estiver lá. A
   tela **Pendrive** faz isso se a partição aparecer na lista dela; senão,
   arraste você mesmo.

Agora você pode iniciar pelo pendrive.

!!! danger "Antes de entrar em qualquer serviço da Apple"
    Cada `config.plist` vem com um número de série, MLB e UUID próprios, mas
    todo mundo que baixa o mesmo arquivo compartilha esses valores, e a `ROM` é
    um valor provisório (`11:22:33:44:55:66`) porque precisa ser o endereço MAC
    da sua própria máquina.

    Gere os seus seguindo os passos de [Pós-instalação](post-installation.md)
    antes de entrar no iCloud, iMessage ou FaceTime.

!!! tip "Se você tem um Mac e a máquina de destino usa BIOS legado"
    Há um terceiro caminho: gerar um instalador offline completo, com a EFI e a
    inicialização legada num só pendrive, dentro de uma imagem de disco que você
    pode clonar de novo depois. Veja [Preparar o pendrive num
    Mac](mac-installer.md).

[Configure a BIOS :material-arrow-right:](bios.md){ .md-button .md-button--primary }
