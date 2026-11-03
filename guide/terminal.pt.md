---
title: Sem a janela
---

# Sem a janela

Tudo o que o app faz pode ser feito sem ele. Um destes caminhos é a resposta se
o app não rodar no seu sistema, se você estiver trabalhando por SSH, ou se
preferir ver os comandos.

Todos geram a mesma pasta EFI; a janela roda o segundo deles e desenha a saída.

## O mesmo construtor num terminal

O `HackintoshEFIBuilder-console-win-x64.zip` em [Releases](https://github.com/yusufklncc/Hackintosh-for-All-Computers/releases) é
o `EFIBuilderEngine.exe` sozinho, para Windows. Ele leva tudo dentro dele, igual
ao app, e faz as mesmas perguntas na mesma ordem:

```
EFIBuilderEngine.exe                        o construtor
EFIBuilderEngine.exe --check                só a leitura do hardware, e sai
EFIBuilderEngine.exe --report machine.json  grava o relatório desta máquina
EFIBuilderEngine.exe --machine machine.json gera para a máquina daquele arquivo
```

O Smart App Control bloqueia este pelo mesmíssimo motivo que bloqueia o app;
veja [Se o seu sistema bloquear](blocked.md).

Para ver as mensagens em português, defina `HFAC_LANG=pt` antes de rodar.

## A partir de um clone

Precisa do Python 3.11 e de mais nada: nenhum pacote para instalar, nenhuma
rede. Funciona no Windows, no Linux e no macOS.

```
python3 tools/setup.py                        o construtor
python3 tools/setup.py --check                só a leitura do hardware
python3 tools/setup.py --machine machine.json gera para outra máquina
python3 tools/detect.py --report machine.json grava o relatório desta máquina
```

O pendrive e o download do recovery são ferramentas próprias, e as telas do app
são estas:

```
python3 tools/recovery.py --list
python3 tools/recovery.py --macos 12.7.6 --out /Volumes/USB

python3 tools/stick.py --list
python3 tools/stick.py --prepare disk4        apaga o disco, e avisa duas vezes
python3 tools/stick.py --place /Volumes/USB --efi build/EFI --recovery .
```

O `--prepare` só lista discos removíveis e externos, nunca o disco pelo qual o
computador iniciou, e pede o disco pelo nome dele antes de começar.

## Formatando o pendrive você mesmo

Um pendrive para o caminho do recovery é simples: **Mapa de Partição GUID** com
uma única partição **MS-DOS (FAT)**. No macOS isso é o Utilitário de Disco com
*Visualizar → Mostrar Todos os Dispositivos*, selecionando o próprio disco e não
o volume abaixo dele, ou:

```
diskutil list                                        # ache o número do disco
diskutil eraseDisk MS-DOS USB GPT /dev/diskN         # N é esse número
```

Depois coloque `EFI/` e `com.apple.recovery.boot/` na raiz dele, lado a lado,
como em [Prepare o pendrive](usb.md).

## Sem script nenhum

O `EFI-base.zip` e o `configs.zip` na mesma release são o caminho manual.

- Extraia o `EFI-base.zip`. Você recebe uma pasta `EFI`, a mesma para todas as
  máquinas, porque o OpenCore carrega só o que a config cita. É também por isso
  que ela tem uns 7 MB e não um gigabyte.
- Abra o `configs.zip` e ache a entrada que combina com o seu hardware.
  Exemplo:
  - o meu processador é um `i5-7200U`. É um processador `Kaby Lake Mobile (Laptop)`, e o notebook é HP.
  - então eu pego `Laptop/HP/009 - Laptop - Kaby Lake.plist`.
  - se não houver entrada para a sua marca, pegue a genérica: `Laptop/009 - Laptop - Kaby Lake.plist`.
- Copie esse arquivo para `EFI/OC/` e renomeie para `config.plist`.
- Copie a pasta `EFI` para a partição EFI do pendrive.

Nada é detectado neste caminho, então nada é adicionado para a sua placa de
rede: veja *Adicionando um kext à mão* abaixo.

## Gerando uma config você mesmo

Para escolher outra versão do OpenCore, ou porque a sua combinação não está na
lista, o repositório gera essas pastas a partir de um pequeno conjunto de
perfis:

```
python3 tools/build.py --catalogue                 # lista todas as configs publicadas
python3 tools/build.py --name "Laptop/HP/009 - Laptop - Kaby Lake"
python3 tools/build.py --platform laptop --cpu kaby-lake --oem hp
```

Não precisa de nada além do Python 3.11 e de um clone. Veja o [tools/README.md](https://github.com/yusufklncc/Hackintosh-for-All-Computers/blob/main/tools/README.md) (em inglês).

## Adicionando um kext à mão

O construtor faz isso por você, e ele conhece 531 ids de dispositivos e qual
kext atende cada um. Este é o caminho se você estiver usando os zips da release,
ou se tiver um hardware que ele não cobre.

Desligue, inicie de volta no Windows e baixe o kext que a sua placa precisa:

| Placa | Kext |
|---|---|
| Wi-Fi Intel | [itlwm](https://github.com/OpenIntelWireless/itlwm/releases) |
| Ethernet Intel | [IntelMausi](https://github.com/acidanthera/IntelMausi/releases) |
| Ethernet Realtek RTL8111 | [RTL8111_driver_for_OS_X](https://github.com/Mieze/RTL8111_driver_for_OS_X/releases) |
| Ethernet Realtek RTL810x | [RealtekRTL8100](https://www.insanelymac.com/forum/files/file/259-realtekrtl8100-binary/) |
| Ethernet Realtek RTL8125 | [LucyRTL8125Ethernet](https://github.com/Mieze/LucyRTL8125Ethernet) |
| Wi-Fi Broadcom | [AirportBrcmFixup](https://github.com/acidanthera/airportbrcmfixup/releases) |
| Wi-Fi Atheros | [Lista da Dortania](https://dortania.github.io/Wireless-Buyers-Guide/Kext.html#atheros) |

1. Coloque o `.kext` em `EFI/OC/Kexts`.
2. Abra o `config.plist` no Bloco de Notas ou no Notepad++ e procure `Kernel`
   com ++ctrl+f++.

    ![A seção Kernel de uma config](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/config-kernel.png)

3. Vá até o fim da seção `Add` e adicione uma entrada para o kext, seguindo o
   formato das entradas que já estão lá.

## Descobrindo o seu hardware você mesmo

O construtor lê tudo isso para você, então isto só é necessário se você quiser
conferir uma máquina antes de começar, ou antes de comprar uma.

Baixe e instale o [AIDA64 Extreme](https://www.aida64.com/downloads), abra e
clique duas vezes em **Summary** (Resumo). Isso mostra o processador, a
placa-mãe, a placa de vídeo e o adaptador de áudio.

=== "Desktop"

    ![Resumo do AIDA64 num desktop](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/aida64-summary.png)

=== "Notebook"

    ![Resumo do AIDA64 num notebook](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/aida64-summary-2.png)

O modelo do disco, as placas de rede e o touchpad são o resto do que importa.

- **Storage → Physical Drives** (armazenamento, discos físicos)

    ![Armazenamento no AIDA64](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/aida64-storage.png)

- **Network → Windows Network** (rede)

    ![Rede no AIDA64](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/aida64-network.png)

- **Devices → PCI Devices** (dispositivos PCI) para o touchpad. Normalmente ele
  é PS/2 ou I²C.

    ![Dispositivos PCI no AIDA64](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/aida64-devices-pci.png)

Essas capturas de tela são da máquina em que este guia foi escrito, que mostra:

| | |
|---|---|
| Modelo | Lenovo ThinkPad E570 |
| Processador | Intel Core i5-7200U |
| Vídeo integrado | Intel HD Graphics 620 |
| Áudio | Conexant CX20753/4 |
| Disco | KBG40ZNV256G KIOXIA NVMe 256GB, Samsung SSD 860 EVO 250GB |
| Rede | Dell Wireless 1820A Wi-Fi + Bluetooth, Realtek RTL8111/8168/8411 Ethernet |
| Touchpad | SynPS/2 Synaptics TouchPad |
