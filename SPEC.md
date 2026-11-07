# Especificação Técnica — Sistema de Consulta de Preços Kiosk (Supermercado)

## 1. Visão Geral do Projeto
O **Consulta Preço Gmais** é um sistema de consulta de preços para supermercados desenvolvido para operar em tablets Android fixados em gôndolas/corredores. O sistema consiste em:
1. **Servidor Local (Backend)**: Aplicação leve rodando em um PC/Servidor local na rede da loja, responsável por autenticar e consumir a **API RP Info (RP Services v2.0.83)**, gerenciar cache/tokens e expor uma API REST unificada.
2. **Aplicativo Android (Kiosk Tablet)**: Aplicativo executado em modo Kiosk (tela travada, sem acesso a configurações, barra de navegação ou sair do app), conectado via rede local (Wi-Fi / Ethernet) ao servidor local e equipado com um leitor de código de barras USB conectado via cabo OTG (modo USB HID / teclado).

---

## 2. Arquitetura do Sistema

```
[Leitor Código de Barras USB]
             │ (Cabo OTG / USB HID - Emulação Teclado)
             ▼
[Tablet Android (Modo Kiosk)]
             │ (HTTP REST via Wi-Fi / Rede Local)
             ▼
[Servidor Local (Python / FastAPI)]
             │ (API REST com Token Cache)
             ▼
[API RP Info (RP Services - Servidor Central / Retaguarda)]
```

---

## 3. Servidor Local (Backend)

### 3.1 Tecnologias
- **Linguagem**: Python 3.10+
- **Framework**: FastAPI + Uvicorn
- **Cliente HTTP**: Requests / Httpx
- **Gerenciamento de Token**: Cache em memória com renovação automática antes da expiração (baseado em `expiresIn` / `tokenExpiration` da API RP Info).

### 3.2 Endpoints Expostos pelo Servidor Local
- `GET /health` — Health check do servidor e status da conexão com a API RP Info.
- `GET /api/product/{barcode}` — Consulta o produto pelo código de barras na API RP Info para a unidade configurada (CNPJ).
  - **Parâmetros**: `barcode` (path), `cnpj` (query opcional ou configurado no ambiente).
  - **Retorno**:
    ```json
    {
      "status": "ok",
      "product": {
        "codigo": 12345,
        "codigoBarras": "7891000123456",
        "descricao": "REFRIGERANTE COCA COLA 2L",
        "preco": 9.99,
        "precoAnterior": 11.49,
        "unidadeMedida": "UN",
        "imagemUrl": "http://servidor/imagens/7891000123456.jpg",
        "estoque": 150.0
      }
    }
    ```

### 3.3 Integração com API RP Info
- **Autenticação**: `POST /v1.1/auth` usando credenciais configuradas (`usuario`, `senha`). Header: `token: <valor>`.
- **Consulta de Produto por Código de Barras**:
  - Endpoint RP Info: `GET /v2.8/produtounidade/{codigoBarras}/unidade/{CNPJ}/consultarcodigobarras` ou `GET /v2.8/produtounidade/{codigoBarras}/unidade/{CNPJ}/estoquecodigobarras`.
  - Tratamento de formatos de resposta (array direto, objeto com chave, objeto aninhado).

---

## 4. Aplicativo Android (Tablet Kiosk)

### 4.1 Requisitos de Kiosk (Modo Bloqueado)
- **Lock Task Mode (App Pinning / Device Owner)**: O aplicativo solicita modo de fixação de tarefa para impedir que o cliente feche o app, acesse a barra de status, notificações ou configurações do Android.
- **Inicialização Automática**: Broadcast Receiver para iniciar automaticamente (`BOOT_COMPLETED`) assim que o tablet for ligado.
- **Sem Barra de Navegação**: Modo imersivo em tela cheia (`SYSTEM_UI_FLAG_IMMERSIVE_STICKY`).

### 4.2 Leitor de Código de Barras via USB OTG
- Os leitores de código de barras USB padrão operam em **modo HID (USB Keyboard)**.
- O aplicativo intercepta eventos de teclado (`dispatchKeyEvent` / `onKeyDown`).
- Quando caracteres chegam rapidamente seguidos de uma tecla Enter (`\n`), o leitor preenche o código de barras e dispara automaticamente a consulta à API do servidor local.

### 4.3 Interface Gráfica (UI/UX)
- **Tela Inicial (Ocioso)**:
  - Logotipo do Supermercado Gmais.
  - Mensagem em destaque: **"Aproxime o código de barras do produto no leitor"** com animação convidativa.
- **Tela de Resultado do Produto**:
  - **Foto do Produto** em alta resolução (carregada via URL do servidor ou cache local).
  - **Nome Completo do Produto** (fonte grande e legível).
  - **Preço Atual** em destaque gigante (ex: `R$ 9,99`).
  - **Preço Anterior / Oferta** (se aplicável).
  - **Indicador de Status** discreto (Conectado / Sincronizado).
  - **Timeout Automático**: Após 8 segundos sem interação, a tela retorna automaticamente para o estado ocioso.

---

## 5. Deployment e Operação
1. **Servidor Local**: Configurar a máquina na retaguarda da loja com IP fixo na rede local, instalar Python, configurar variáveis de ambiente (`RP_HOST`, `RP_USER`, `RP_PASS`, `RP_CNPJ`) e executar o servidor via Uvicorn como serviço do Windows/Linux (`nssm` ou `systemd`).
2. **Tablets**:
   - Conectar o leitor de código de barras USB via cabo OTG na porta USB do tablet.
   - Instalar o APK do aplicativo.
   - Configurar o IP do servidor local na tela de configurações iniciais do app (protegida por PIN de administrador).
   - Ativar o modo Kiosk no tablet.
