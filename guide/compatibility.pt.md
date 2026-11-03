---
title: Confira a compatibilidade
---

# Confira a compatibilidade

A tela **Hardware compatível** lista 766 dispositivos em 8 categorias, tudo o
que este repositório conhece, com busca por nome, id ou kext. A tela **Máquina**
responde a mesma pergunta sobre o computador que você está usando.

Para hardware que nenhuma das duas cobre, estes são os guias que vale ler antes
de comprar qualquer coisa (em inglês).

- [Anti-Hackintosh Buyers Guide](https://dortania.github.io/Anti-Hackintosh-Buyers-Guide/)
- [Processadores](https://dortania.github.io/Anti-Hackintosh-Buyers-Guide/CPU.html#cpus-to-avoid)
- [Placas de vídeo](https://dortania.github.io/GPU-Buyers-Guide/)
- [Placas-mãe](https://dortania.github.io/Anti-Hackintosh-Buyers-Guide/Motherboard.html)
- [Armazenamento](https://dortania.github.io/Anti-Hackintosh-Buyers-Guide/Storage.html)
- [Placas Wi-Fi](https://dortania.github.io/Wireless-Buyers-Guide/unsupported.html)

## O que nenhum guia diz

Uma geração pode ter suporte enquanto uma peça dela não tem. Esses casos ficam
registrados em `data/field.toml` com o nome de quem observou, e o construtor
avisa sobre eles:

!!! note "Intel Core i5-10200H"
    O macOS instala, mas o vídeo integrado nunca tem aceleração. Comet Lake tem
    suporte como geração, então só a regra da geração diria que este também
    tem.

    *Observado por yusufklncc.*

!!! note "Wi-Fi Broadcom, a partir do macOS 14"
    O `AirportBrcmFixup` faz patches no próprio driver Broadcom da Apple em vez
    de substituí-lo, e a Apple removeu esses drivers, um de cada vez, então as
    placas não param todas no mesmo ponto. O README do kext lista, por versão
    do macOS, quais ids cada driver ainda atende:

    | Placa | Funciona até |
    |---|---|
    | `43a0`, `43a3`, `43ba` | **Ventura**; depois *"[14+] Use with OCLP"*, `AirPortBrcmNIC: removed` |
    | `4331`, `4353` | **Catalina**; no `[11]`, `AirPortBrcm4360: removed` |
    | `432b` | **Mojave**; no `[10.15]`, `AirPortBrcm4331: removed` |

    Acima do seu próprio limite, uma placa precisa dos root patches do
    OpenCore Legacy Patcher no sistema instalado; nada que uma EFI injete
    consegue fazer isso.

    O kext também reconhece outros ids Broadcom, e essa tabela nunca cita
    eles. Para esses o construtor diz isso claramente em vez de inventar uma
    faixa.

    O construtor avisa quando você pede um macOS acima do limite, em vez de
    adicionar um kext que nunca vai carregar.

    *Observado num Dell Wireless 1820A por yusufklncc: num recovery do Sequoia
    o ícone do Wi-Fi aparece depois que os drivers antigos são injetados à mão,
    diz que está conectado e não lista nenhuma rede. Um recovery não tem
    nenhum dos root patches, então isso é esperado.*

Placas Wi-Fi Realtek não têm driver nenhum no macOS. Se é isso que o seu
notebook tem, um cabo de rede durante a instalação é o jeito de contornar: veja
[Prepare o pendrive](usb.md).
