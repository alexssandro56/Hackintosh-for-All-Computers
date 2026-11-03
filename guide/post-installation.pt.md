---
title: Pós-instalação
---

# Pós-instalação

Dois ajustes de arrumação, e depois a única coisa que precisa mesmo ser feita.

## Arrume a config

Abra o `config.plist` com o TextEdit.

- Procure `HideAuxiliary` e troque `false` por `true`: isso esconde as opções
  extras do menu de inicialização.
- Procure `boot-args` e apague o `-v`: isso para o texto do modo verbose a cada
  inicialização.

!!! note "Deixe o `SecureBootModel` em `Disabled`"
    Guias para outras configurações mandam aumentar esse valor, e para essas
    configurações eles estão certos. Aqui não.

    Qualquer outro valor se recusa a iniciar versões do macOS lançadas antes
    daquele modelo de Mac, e este repositório oferece imagens desde o Yosemite.
    A partir do macOS 12 o valor também precisa combinar com o SMBIOS, e 101 das
    configs daqui usam um modelo de Mac anterior ao chip T2, que não tem nenhum
    modelo de Secure Boot. Além disso, o Apple Secure Boot rejeita extensões de
    kernel sem assinatura, que é quase tudo o que esta EFI injeta.

## Coloque o seu próprio endereço MAC na `ROM`

**Esta é a que não é opcional.** Toda EFI gerada vem com a `ROM` num valor
provisório, e nenhum construtor tem como saber o seu de antemão. iCloud,
iMessage e FaceTime não vão funcionar até você fazer isso.

1. Vá em **Ajustes do Sistema → Rede → Ethernet → Detalhes → Hardware** e veja
   o seu endereço MAC.
2. Tire os dois-pontos: `54:1A:AF:43:70:CA` vira `541AAF4370CA`.
3. Converta isso para [Base64](https://base64.guru/converter/encode/hex). O
   resultado é `VBqvQ3DK`.
4. Coloque em `ROM` e salve.
5. Reinicie, aperte ++space++ no menu do OpenCore e escolha **ResetNVRAM**.

!!! warning "As configurações da sua BIOS podem voltar ao padrão"
    Confira depois de limpar a NVRAM, antes de iniciar o macOS de novo.

## O seu próprio número de série

Cada EFI gerada cria seu próprio número de série, MLB e UUID, então você não
divide um com o repositório inteiro. Mas todo mundo que baixa o mesmo **arquivo
de release** divide. Se você quer um que ninguém mais tenha:

1. Baixe o [GenSMBIOS](https://github.com/corpnewt/GenSMBIOS/archive/refs/heads/master.zip)
   e abra o arquivo `.command`. Se ele oferecer baixar o Python, deixe. Depois
   escolha a opção **3**.

    ![O GenSMBIOS abrindo](https://raw.githubusercontent.com/yusufklncc/Lenovo-Thinkpad-E570-Hackintosh/main/src/GenSMBIOS/GenSMBIOS%201.png)

2. Digite o SMBIOS que a sua config já usa. O construtor mostrou esse valor, e
   ele está em `SystemProductName`.

    ![Digitando o modelo](https://raw.githubusercontent.com/yusufklncc/Lenovo-Thinkpad-E570-Hackintosh/main/src/GenSMBIOS/GenSMBIOS%202.png)

3. Copie o primeiro número de série.

    ![Os números de série gerados](https://raw.githubusercontent.com/yusufklncc/Lenovo-Thinkpad-E570-Hackintosh/main/src/GenSMBIOS/GenSMBIOS%203.png)

4. [Confira com a Apple](https://checkcoverage.apple.com/). Ele deve aparecer
   como inválido ou não comprado. **Se a Apple reconhecer, use o próximo**: um
   número de série que pertence a um Mac de verdade é de outra pessoa.

    ![Conferindo o número de série](https://raw.githubusercontent.com/yusufklncc/Lenovo-Thinkpad-E570-Hackintosh/main/src/GenSMBIOS/Check%20Serial.png)

5. Substitua `SystemSerialNumber`, `MLB` e `SystemUUID` pelos `Serial`,
   `Board Serial` e `SmUUID` que ele gerou, e depois limpe a NVRAM como acima.

!!! tip "Se esse modelo não tiver suporte para o macOS que você instalou"
    Adicione `-no_compat_check` aos `boot-args`.

    Isso faz a inicialização passar pela verificação de modelo; não leva uma
    *instalação* até o fim com uma identidade que a versão não atende. O lugar
    dele é depois da instalação, quando a identidade certa já foi colocada de
    volta.

Agora você pode entrar no iCloud, no iMessage e no resto.
