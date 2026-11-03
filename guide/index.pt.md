---
title: O que é isto
---

# macOS em Todos os Computadores

![Todos os macOS que este repositório cobre](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/All%20macOS.png)

Este repositório instala o macOS em hardware de PC, e faz isso por meio de um
programa que você baixa e roda. O programa lê a máquina em que está rodando,
descobre qual pasta EFI do OpenCore essa máquina precisa, gera essa pasta, baixa
o instalador da Apple, formata o pendrive e copia os dois para ele.

Não há nada para instalar junto e nada para configurar. As tabelas de hardware,
os kexts e os arquivos do OpenCore vêm todos dentro dele, e ele não abre nenhuma
conexão além da que baixa o macOS, quando você clica nesse botão.

![A tela Máquina](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/App/machine.png)

## A versão curta

1. [Baixe o programa](app.md) e rode. Se o seu sistema se recusar a abri-lo,
   [isso é esperado e se resolve com um ajuste](blocked.md).
2. [Responda as perguntas do construtor](efi.md). Ele gera uma pasta `EFI`.
3. [Prepare o pendrive](usb.md): o programa formata, baixa o recovery da Apple
   e copia os dois para ele.
4. [Configure a BIOS](bios.md), inicie pelo pendrive e
   [instale o macOS](installation.md).
5. [Defina a sua própria ROM e o seu serial](post-installation.md) antes de
   entrar em qualquer serviço da Apple.

Tudo isso também pode ser feito pelo terminal, ou à mão a partir de dois
arquivos zip. Está tudo numa página só: [Sem a janela](terminal.md). O
resultado é exatamente a mesma pasta EFI.

## O que ele não faz

Ele não chuta. Quando a máquina consegue informar algo, a opção aparece marcada
como *detectado* e mesmo assim quem escolhe é você: a detecção pode errar, e uma
resposta errada que já chega marcada é uma que ninguém confere.

Ele não finge conhecer hardware sobre o qual não tem dados. `desconhecido` ao
lado de um dispositivo quer dizer que nenhuma tabela aqui diz nada sobre ele, e
não que ele falhe.

Ele não redistribui software da Apple. Nenhum instalador, nenhum BaseSystem,
nenhuma imagem: o download do recovery vem da Apple, pelo protocolo da própria
Apple, usando a ferramenta que o OpenCore fornece para isso. Os ícones das
versões do macOS na tela Recovery são da Apple e estão ali para identificar a
qual versão cada quadro se refere.

!!! question "Algo deu errado"
    Abra uma issue com o que você tem e o que aconteceu. A tela **Relatório**
    gera um `machine.json` sem nenhum número de série; anexar ele transforma um
    palpite numa resposta.
