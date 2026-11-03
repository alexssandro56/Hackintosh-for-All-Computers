---
title: Se o seu sistema bloquear
---

# Se o seu sistema bloquear

Assinar um aplicativo significa pagar todo ano à Microsoft ou à Apple por um
certificado. Este projeto não paga, então a primeira execução é recusada nos
dois sistemas.

Nada abaixo enfraquece nada de forma permanente, e nada disso é exclusivo deste
programa: é o que todo download de código aberto sem assinatura precisa.

## Windows

Se o **Controle Inteligente de Aplicativos** (Smart App Control) estiver ligado,
o programa não abre e o Windows explica muito pouco do motivo. A página da
própria Microsoft é clara sobre a regra:

> If the app is unsigned, or the signature is invalid, Smart App Control will
> consider it untrusted and block it for your protection.
>
> — [What is Smart App Control?](https://support.microsoft.com/en-us/topic/what-is-smart-app-control-285ea03d-fa88-4d56-882e-6698afdb7003)

Ou seja: se o app não é assinado, ou a assinatura é inválida, o recurso o
considera não confiável e o bloqueia. Não existe *executar mesmo assim* nessa
janela. Desligar o recurso é o único jeito de passar.

1. Abra a **Segurança do Windows**.
2. Vá em **Controle de aplicativos e do navegador** → **Controle Inteligente de
   Aplicativos**.
3. Coloque em **Desativado**.
4. Rode o programa.

!!! question "Posso ligar de novo depois?"
    Sim. A página da Microsoft responde a pergunta que todo mundo faz antes de
    mexer nisso: *"Recent Windows updates allow Smart App Control to be
    re-enabled without requiring a clean installation."* Ou seja, as
    atualizações recentes do Windows permitem religar sem reinstalar o sistema.
    Religar foi testado aqui no Windows 11 e funcionou pela mesma chave.

### Não foi essa a janela que apareceu

Uma caixa azul com o título **O Windows protegeu o computador** é o SmartScreen,
não o Controle Inteligente de Aplicativos. Esse dá para passar sem mudar nenhuma
configuração:

1. Clique em **Mais informações**.
2. Clique em **Executar assim mesmo**.

## macOS

O app tem uma assinatura ad-hoc, o suficiente para o macOS rodá-lo no Apple
silicon, mas ele não é notarizado, então o Gatekeeper recusa a primeira
abertura.

!!! tip "Mova o app antes de abrir"
    Descompacte o download e **mova o app pelo Finder** antes de abrir. Qualquer
    lugar serve; a pasta Aplicativos é só o costume.

    Quando um app em quarentena é aberto do lugar onde foi descompactado, o
    macOS roda uma cópia somente leitura dele em outro lugar do disco. Isso se
    chama App Translocation, e é por isso que um app pode estar liberado e
    mesmo assim se comportar como se não estivesse. Movê-lo pelo Finder acaba
    com isso.

    Se preferir não mover, remover a marca de quarentena faz o mesmo e deixa o
    app onde está:

    ```
    xattr -dr com.apple.quarantine "Hackintosh EFI Builder.app"
    ```

O caminho é tentar uma vez e depois liberar, nessa ordem:

1. Dê dois cliques em `HackintoshEFIBuilder.app`. **Ele vai ser recusado.** É
   essa recusa que cria a opção do próximo passo.
2. Abra **Ajustes do Sistema** → **Privacidade e Segurança**, role até
   **Segurança** e clique em **Abrir Mesmo Assim** ao lado do nome do app.
3. Digite a sua senha de login.

A Apple avisa que esse *"botão fica disponível por cerca de uma hora depois que
você tenta abrir o app"* ([Abrir um app de um desenvolvedor
desconhecido](https://support.apple.com/guide/mac-help/open-a-mac-app-from-an-unknown-developer-mh40616/mac)).
Se ele não estiver lá, tente abrir o app de novo e volte.

O macOS lembra da exceção, e a partir daí o app abre normalmente.

## Linux

Nada bloqueia. O AppImage só precisa da permissão de execução.

```
chmod +x HackintoshEFIBuilder-linux-x64.AppImage
./HackintoshEFIBuilder-linux-x64.AppImage
```

## Nada disso funcionou

O construtor também roda sem a janela, num terminal, a partir de um pacote que
não tem parte gráfica nenhuma: veja [Sem a janela](terminal.md). Ele faz as
mesmas perguntas e gera a mesma pasta EFI.

No Windows, lembre que o Controle Inteligente de Aplicativos bloqueia esse
pacote pelo mesmo motivo que bloqueia o app; o pacote de terminal não é um jeito
de contornar essa configuração.
