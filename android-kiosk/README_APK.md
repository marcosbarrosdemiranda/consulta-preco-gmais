# Aplicativo Kiosk Android — Consulta Preço Gmais

Este diretório contém o projeto Android Studio nativo em Kotlin para gerar o APK do totem de consulta de preços em modo Kiosk.

## 🚀 Funcionalidades
- **WebView Fullscreen**: Carrega automaticamente a interface do servidor local Gmais (`http://192.168.1.4:48291`).
- **Modo Kiosk / Imersivo**: Oculta a barra de status e botões de navegação, impedindo que usuários saiam da aplicação.
- **Bloqueio do Botão Voltar**: Impede o fechamento acidental da tela.
- **Suporte a Leitor USB OTG**: Compatível com leitores de código de barras USB em modo teclado (HID), cujos eventos de tecla são capturados nativamente pela aplicação web.

---

## 🛠 Como Gerar o APK

1. **Abrir no Android Studio**:
   - Abra o Android Studio e selecione **Open an Existing Project**, apontando para a pasta `android-kiosk`.
2. **Configurar o IP do Servidor**:
   - Abra `app/src/main/java/br/com/gmais/consultapreco/MainActivity.kt`
   - Altere a variável `serverUrl` para o IP do computador onde o servidor Docker está rodando (ex: `http://192.168.1.10:48291`).
3. **Gerar o APK (Build)**:
   - No menu superior, vá em **Build > Build Bundle(s) / APK(s) > Build APK(s)**.
   - O APK gerado estará em `android-kiosk/app/build/outputs/apk/debug/app-debug.apk`.
4. **Instalação no Tablet Android**:
   - Transfira o arquivo `app-debug.apk` para o tablet via USB ou pen-drive OTG.
   - Instale no tablet.
   - *(Opcional)* Defina o aplicativo como **Home App padrão** (Launcher) para que ele abra automaticamente ao ligar o tablet e trave a tela no modo Kiosk.
