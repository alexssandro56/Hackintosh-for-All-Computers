---
title: Gerar para outra máquina
---

# Gerar para outra máquina

A detecção lê o computador em que está rodando. Se você estiver preparando o
pendrive num PC que funciona para usar em outro, tudo o que ela encontra (vídeo,
codec de áudio, placas de rede, NVMe, trackpad) pertence à máquina errada, e
você não quer nada disso na config.

## Com um relatório de hardware

A solução é tirar o relatório na máquina de destino e levar para a outra.

1. Na máquina **para** a qual você vai gerar, rode o programa e abra a tela
   **Relatório**. Ela gera um pequeno arquivo JSON: processador, placa, vídeo,
   ids PCI, USB e de áudio, modelos de NVMe.

    A quarta resposta do Construtor, *Nenhuma: só salvar o relatório desta
    máquina*, faz a mesma coisa.

2. Copie esse arquivo para o computador **onde** você vai gerar a EFI, por
   pendrive, e-mail ou qualquer outro meio. Ele não guarda nenhum número de
   série nem uma lista bruta de dispositivos.

3. Lá, abra o Construtor e responda *Outra máquina, e eu tenho o relatório de
   hardware dela*. Ele pede o arquivo.

A partir daí, toda pergunta e toda recomendação valem para aquela máquina.

## Sem relatório

Responda *Outra máquina, e eu não tenho o relatório*. Nada é detectado e nada é
adivinhado; em vez disso ele pergunta qual Ethernet, Wi-Fi e Bluetooth a máquina
tem, pelo nome, a partir dos drivers que este repositório inclui.

!!! warning "O que um nome não consegue dizer"
    Vídeo, áudio e trackpad precisam do relatório. Eles não podem ser
    descobertos a partir do nome de um modelo, e o construtor não vai fingir
    que pode.
