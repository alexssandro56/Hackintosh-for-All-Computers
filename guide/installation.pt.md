---
title: Passos da instalação do macOS
---

# Passos da instalação do macOS

Inicie pelo pendrive e escolha **Install macOS "Sonoma"**, ou a versão que você
estiver instalando.

![O menu do OpenCore](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/opencore-install-macos.png)
![Início do modo verbose](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/verbose-start.png)
![O modo verbose continuando](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/middle-verbose.png)

Escolha o idioma.

![Escolhendo o idioma do instalador](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/install-macos-select-language.png)

!!! tip "Confira a rede antes de seguir"
    Na Ethernet, clique duas vezes no Safari e veja se uma página carrega. No
    Wi-Fi, clique no ícone do Wi-Fi no canto superior direito, entre na sua rede
    e teste no Safari.

    No caminho do recovery isso não é opcional: o instalador baixa o macOS a
    partir daqui.

## Prepare o disco

Abra o **Utilitário de Disco** (*Disk Utility*).

![Abrindo o Utilitário de Disco](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/open-disk-utility.png)

No botão *Visualizar*, escolha **Mostrar Todos os Dispositivos**.

![Mostrar Todos os Dispositivos](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/show-all-devices.png)

Selecione à esquerda o disco onde vai instalar e clique em **Apagar**.

![Selecionando o disco para apagar](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/select-main-disk-name-erase.png)

Dê um nome ao disco, coloque **Formato** em APFS e **Esquema** em Mapa de
Partição GUID. Clique em **Apagar**.

![Nome, formato e esquema](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/name-format-scheme.png)

=== "Instalando ao lado do Windows"

    Crie antes uma partição em HFS+ ([guia em
    vídeo](https://vk.com/video749455540_456239018)).

    Depois clique com o botão direito no volume que você criou, na barra
    lateral do Utilitário de Disco, e escolha **Converter em APFS**. Você pode
    escolhê-lo na tela do instalador e seguir.

=== "Adicionando um volume a um disco que já tem macOS"

    Selecione o **Contêiner** e clique no botão **+** no canto superior direito.

    ![Adicionando um volume APFS](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/add-apfs-volume.png)

    Dê um nome ao volume, coloque o Formato em APFS e clique em Apagar.

    ![Dando nome ao novo volume](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/name-new-volume.png)

Quando terminar de apagar, clique em **OK**.

![Disco apagado](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/erase-done.png)

## Rode o instalador

Feche o Utilitário de Disco e abra **Install macOS "Sonoma"**.

![Abrindo o instalador](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/open-instal-macos.png)

Clique em **Continuar**, depois em **Concordar** e mais uma vez em
**Concordar**.

![Instalador, passo um](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/install-macos-1.png)
![Instalador, passo dois](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/install-macos-2.png)
![Instalador, passo três](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/install-macos-3.png)

Selecione o disco que você apagou e clique em **Continuar**.

![Selecionando o disco de destino](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/install-macos-select-disk.png)
![A instalação começando](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/install-macos-start.png)
![A instalação em andamento](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/install-macos-middle.png)

Por volta de **12 minutos restantes** o computador reinicia no modo verbose.

![A primeira reinicialização](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/first-restart.png)

!!! warning "Qual opção iniciar depois de cada reinicialização"
    O OpenCore cria uma entrada de inicialização chamada **OpenCore**, e a
    máquina vai usá-la em toda reinicialização daqui em diante. Alguns
    firmwares recusam entradas personalizadas; se você tem outro sistema
    operacional neste computador, escolha o pendrive no menu de inicialização
    a cada reinicialização.

Depois da primeira reinicialização, escolha **macOS Installer** no menu do
OpenCore.

![Escolhendo macOS Installer](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/first-restart-macos-installer.png)

Aparecem o logo da Apple e uma barra de tempo, e depois outra reinicialização.

![A segunda etapa](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/second-installation.png)
![A segunda reinicialização](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/second-restart.png)

Continue escolhendo **macOS Installer** até essa opção sumir. Na última
reinicialização aparece o nome que você deu ao disco: escolha esse.

![Escolhendo o disco instalado](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/last-select-disk.png)

## Configure o macOS

Escolha o seu país.

![Escolhendo o país](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/select-country.png)

Aqui o guia clica em **Personalizar Ajustes**, porque a máquina é usada em
inglês enquanto o teclado e o idioma nativo não são. Se o padrão servir para
você, clique em Continuar.

![Idioma](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/select-language.png)
![Fonte de entrada](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/select-input.png)
![Fonte de entrada, continuação](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/select-input-2.png)
![Ditado](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/select-dictation.png)

Pule a acessibilidade com **Agora Não**.

![Acessibilidade](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/accessibility.png)

!!! danger "Escolha *Meu computador não se conecta à internet*"
    Mesmo que a sua conexão funcione. O número de série, o MLB e a ROM da sua
    config ainda precisam ser só seus antes que esta máquina fale com a Apple:
    veja [Pós-instalação](post-installation.md).

![Configuração de rede](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/select-network-type.png)
![Configuração de rede, continuação](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/select-network-type-2.png)

Clique em **Continuar**.

![Dados e privacidade](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/data-privacy.png)

O Assistente de Migração pode trazer dados de outra máquina. Supondo que esta
seja a primeira instalação, clique em **Agora Não**.

![Assistente de Migração](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/migration-assistant.png)

Clique em **Concordar** e mais uma vez em **Concordar**.

![Termos e condições](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/terms-conditions.png)
![Termos e condições, continuação](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/terms-conditions-2.png)

Crie uma conta com nome, nome de usuário e senha.

![Criando a conta](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/create-account.png)

Serviços de Localização, análises, Tempo de Uso e Siri ficam a seu critério. O
guia desliga as análises.

![Serviços de Localização](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/enable-location.png)
![Análises](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/analytics.png)
![Tempo de Uso](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/screen-time.png)
![Siri](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/enable-siri.png)
![Idioma da Siri](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/select-siri-language.png)
![Voz da Siri](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/select-siri-voice.png)
![Melhorar a Siri e o Ditado](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/improve-siri-dictation.png)

Escolha um tema, e a instalação terminou.

![Escolhendo um tema](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/select-theme.png)

Talvez apareça o assistente de configuração do teclado depois. Siga os passos
dele.

![Assistente de Configuração do Teclado](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/keyboard-setup-assistant.png)
![Identificando o teclado](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/identifying-keyboard.png)
![Escolhendo o tipo de teclado](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/select-keyboard-type.png)

E aí está a área de trabalho.

![A área de trabalho](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/desktop-2.png)
![A tela de bloqueio](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/lock-screen.png)

!!! bug "Ajustes do Sistema ou Sobre Este Mac fecha sozinho ao abrir"
    Abra o Terminal e rode `sudo purge`.

    ![O travamento](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/system-settings-crash.png)
    ![Terminal no Spotlight](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/spotlight-terminal.png)
    ![sudo purge](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/sudo-purge.png)
    ![sudo purge, terminando](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/sudo-purge-2.png)
    ![Sobre Este Mac](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/about-this-mac.png)
    ![Ajustes do Sistema](https://raw.githubusercontent.com/yusufklncc/Hackintosh-for-All-Computers/main/Resources/Installation/system-settings.png)

[Pós-instalação :material-arrow-right:](post-installation.md){ .md-button .md-button--primary }
