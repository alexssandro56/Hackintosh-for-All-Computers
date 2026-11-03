---
title: Configure a BIOS
---

# Configure a BIOS

Nem todas estas opções vão existir no seu firmware. Deixe o mais parecido que
conseguir e não se preocupe com as que faltarem.

**Restaure a BIOS para o padrão de fábrica antes de começar.**

=== "Intel"

    **Desative**

    - Fast Boot
    - Secure Boot
    - Serial/COM Port
    - Parallel Port
    - Compatibility Support Module (CSM)
    - Thunderbolt
    - Intel SGX
    - Intel Platform Trust
    - CFG Lock (proteção de escrita do MSR 0xE2)

    **Ative**

    - VT-x
    - Above 4G decoding
    - Hyper-Threading
    - Execute Disable Bit
    - EHCI/XHCI Hand-off
    - Tipo de sistema: Windows 8.1/10 UEFI Mode (algumas placas precisam de *Other OS*)
    - DVMT Pre-Allocated (memória do iGPU): 64MB ou mais
    - SATA Mode: AHCI

    !!! danger "O CFG Lock precisa estar desligado"
        A sua máquina não vai iniciar com o CFG-Lock ativado. Se a opção não
        existir no seu firmware, ative `AppleXcpmCfgLock` em
        **Kernel → Quirks** na config.

    !!! warning "CSM"
        Precisa estar desligado na maioria dos casos. Erros de vídeo e
        travamentos como o `gIO` são comuns quando ele está ligado.

    !!! note "Thunderbolt"
        Desligado na primeira instalação. O Thunderbolt causa problemas se não
        estiver configurado do jeito certo, e configurá-lo é tarefa para depois
        que o macOS estiver rodando.

=== "AMD Ryzen"

    **Desative**

    - Fast Boot
    - Secure Boot
    - Serial/COM Port
    - Parallel Port
    - Compatibility Support Module (CSM)
    - IOMMU

    **Ative**

    - Above 4G Decoding
    - EHCI/XHCI Hand-off
    - Tipo de sistema: Windows 8.1/10 UEFI Mode (algumas placas precisam de *Other OS*)
    - SATA Mode: AHCI

    !!! danger "O Above 4G Decoding precisa estar ligado"
        Se você não encontrar a opção, adicione `npci=0x3000` aos `boot-args`.
        Não deixe os dois ativados ao mesmo tempo.

        Em placas Gigabyte/Aorus e ASRock, ativar pode quebrar drivers como o
        da Ethernet ou impedir outros sistemas de iniciar. Se isso acontecer,
        desligue e use o `npci` no lugar.

    !!! warning "Resizable BAR, em firmwares de 2020 em diante"
        Ativar o Above4G pode liberar o **Resizable BAR Support** em algumas
        placas X570 e mais novas. Se ele estiver ativado, coloque
        **Booter → Quirks → ResizeAppleGpuBars** em `0`.

    !!! note "Threadripper 3990X"
        O kernel do macOS dá pânico acima de 64 threads. O 3990X tem 128, então
        metade precisa sair: desative o hyper-threading na BIOS.

[Primeira inicialização :material-arrow-right:](first-boot.md){ .md-button .md-button--primary }
