---
title: Gere a sua EFI
---

# Gere a sua EFI

Abra a tela **Construtor** e clique em começar. Ele faz algumas perguntas e gera
a pasta.

Quando consegue ler a resposta da sua máquina, ele avisa ao lado da pergunta,
mas nunca escolhe por você: a detecção pode errar, e uma resposta errada que já
chega marcada é uma que ninguém confere.

## O que o seu hardware significa para o macOS

Primeiro ele diz o que encontrou:

```
Hardware para o macOS  de esta máquina

  CPU          Intel(R) Core(TM) i5-4200U CPU @ 1.60GHz  suportado     haswell, perfil de notebook
  Vídeo        Intel(R) HD Graphics Family  [8086:0a16]  suportado     iGPU Intel, haswell
  Áudio        Realtek ALC283                            suportado     AppleALC, 11 layouts para testar
  Ethernet     Intel Ethernet                            suportado     IntelMausi.kext  [8086:1559]
  Wi-Fi        Intel Wi-Fi                               suportado     AirportItlwm.kext  [8086:08b3]
  Bluetooth    Intel Bluetooth                           suportado     IntelBluetoothFirmware.kext
  Disco        sem NVMe                                  -             nada a adicionar
  Trackpad     Alps Pointing-device                      suportado     em PS/2, que o VoodooPS2 cobre
  Câmera       TOSHIBA Web Camera - FHD                  suportado     USB, então o driver genérico atende
  Leitor de cartão  Realtek PCIE CardReader              desconhecido  sem dados de suporte para leitores de cartão

  Nada aqui é sabidamente sem suporte.
```

`desconhecido` quer dizer que nenhuma tabela aqui tem algo a dizer sobre aquela
peça, e não que ela vá falhar. Nada nesta tela impede a geração: se uma placa
não tiver suporte, ele avisa e sugere trocá-la, e a escolha continua sendo sua.

A tela **Máquina** mostra a mesma leitura a qualquer momento, sem começar uma
geração.

## As perguntas

```
[1] Para qual máquina é esta EFI?
      detectado: Esta máquina
       1) Esta máquina <- detectado
       2) Outra máquina, e eu tenho o relatório de hardware dela
       3) Outra máquina, e eu não tenho o relatório
       4) Nenhuma: só salvar o relatório desta máquina, para gerar a EFI em outro lugar
      > 1

[2/5] Que tipo de máquina é esta?
      detectado: Notebook
       1) Desktop
       2) Notebook <- detectado
      > 2

[3/5] Qual a geração do processador?
      detectado: Kaby Lake
      ...
      10) Kaby Lake <- detectado
      > 10

[4/5] Marca da placa-mãe ou do notebook?
      detectado: hp
       3) HP <- detectado
      > 3

[5/5] Qual macOS você vai instalar?
      ...
```

A **primeira** pergunta importa porque o pendrive costuma ser feito num
computador que já funciona, e não no que está sendo convertido. Veja [Gerar para
outra máquina](another-machine.md).

### Qual macOS e por que não é só sobre kexts

Uma config finge ser um modelo de Mac, e o macOS decide o que vai instalar a
partir desse modelo, e não a partir do seu hardware.

!!! example "A falha que isto evita"
    Peça o Tahoe numa config que finge ser um `MacBookPro14,1` e a instalação
    para sem dizer o motivo, porque a Apple só oferece até o Ventura para esse
    modelo.

O construtor confere isso antes de você chegar lá. Se o modelo do seu perfil não
recebe a versão que você pediu, ele cita os que recebem e oferece trocar por um,
começando pela mesma família e nunca pelo modelo que já está em uso. Se você
recusar, ele gera o que você pediu e avisa o que vai acontecer.

## O que ele oferece pelo caminho

Nada disto é perguntado a menos que as suas respostas tornem relevante, e tudo
pode ser recusado.

<div class="grid cards" markdown>

-   **SSDTs**

    Ele abre o SSDTTime dentro da janela para os patches que a sua plataforma
    precisa, e você segue o menu da própria ferramenta ali mesmo.

-   **Portas USB**

    Mapear agora, nesta máquina, gera o mapa de portas que o macOS precisa em
    vez do genérico.

-   **Framebuffer e device-id**

    No vídeo Intel ele oferece o id de framebuffer do seu chip e, quando a
    documentação do WhateverGreen diz que é preciso falsificar o device-id
    (as peças Ice Lake G1 entre elas), oferece isso também, citando a frase de
    onde tirou.

-   **Trackpad**

    Um trackpad I²C ou SMBus é perguntado à parte, porque PS/2 e SMBus precisam
    de kexts diferentes.

</div>

## Placas de rede

Por último, porque sem uma a máquina não consegue terminar a instalação:

```
  Ethernet
      8086:15b8  needs IntelMausi.kext        Intel Ethernet, v1.0.8
  Wi-Fi
      8086:2723  needs AirportItlwm.kext      Intel Wi-Fi, v2.3.0

Adicionar estes à EFI?
   1) Sim, para todas as versões do macOS que eles suportam
   2) Sim, só para uma versão do macOS
   3) Não, deixar de fora
```

Escolher **todas as versões** coloca cada kext com a faixa de macOS a que ele
se aplica e deixa o OpenCore carregar o certo, então uma EFI só inicia qualquer
um deles. Escolher **uma versão** coloca só o que aquela versão precisa.

O Wi-Fi Intel é a exceção: ele é compilado separadamente para cada macOS, então
sempre pergunta qual.

---

Depois ele gera a pasta `EFI` e oferece abri-la.

[Prepare o pendrive :material-arrow-right:](usb.md){ .md-button .md-button--primary }
