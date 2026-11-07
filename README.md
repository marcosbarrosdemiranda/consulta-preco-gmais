# Consulta Preço Gmais — Kiosk Android + Servidor Local (API RP Info)

Sistema de consulta de preços para supermercados desenvolvido para tablets Android em modo Kiosk, conectado via USB OTG a leitores de código de barras e comunicando-se com um servidor local integrado à **API RP Info (RP Services)**.

---

## 📁 Estrutura do Projeto

```
├── SPEC.md                    # Especificação técnica completa do projeto
├── README.md                  # Este manual de instruções
└── server/
    ├── main.py                # Servidor FastAPI (integração RP Info + API REST)
    ├── run_server.py          # Script de inicialização do servidor local
    ├── requirements.txt       # Dependências Python
    ├── .env.example           # Template de variáveis de ambiente
    └── static/
        └── index.html         # Interface Kiosk Web (otimizada para tablets, leitor USB OTG)
```

---

## 🚀 Como Executar o Servidor Local

1. **Instalar dependências Python**:
   ```bash
   cd server
   pip install -r requirements.txt
   ```

2. **Configurar as credenciais da API RP Info**:
   Copie `.env.example` para `.env` e ajuste os parâmetros da sua loja:
   ```env
   RP_HOST=http://servicosflex.rpinfo.com.br:9000
   RP_USER=seu_usuario
   RP_PASS=sua_senha
   RP_CNPJ=seu_cnpj_unidade
   PORT=8000
   HOST=0.0.0.0
   ```

3. **Iniciar o servidor**:
   ```bash
   python run_server.py
   ```
   O servidor iniciará em `http://localhost:8000` (ou no IP local da máquina na rede da loja).

---

## 📱 Configuração do Tablet Android (Kiosk & Leitor USB OTG)

1. **Leitor de Código de Barras USB**:
   - Conecte o leitor de código de barras USB no tablet Android utilizando um **cabo adaptador OTG (USB / Tipo-C)**.
   - O leitor deve estar configurado em **modo USB HID (Teclado)** — padrão de fábrica da maioria dos leitores. Quando um código for lido, o leitor digita os caracteres e envia um `Enter`.
   - A interface web intercepta automaticamente os eventos de teclado e realiza a consulta.

2. **Aplicativo Android (Modo Kiosk)**:
   - Para transformar o tablet em um terminal de consulta dedicado:
     - **Opção A (WebView Wrapper)**: Crie um projeto Android simples (WebView) apontando para o IP do servidor local (`http://<IP_DO_SERVIDOR>:8000`).
     - **Opção B (App Pinning nativo)**: Utilize o recurso nativo de Fixação de Tela (App Pinning) do Android nas configurações de segurança do tablet para travar o aplicativo em tela cheia.
     - **Opção C (Launchers Kiosk Dedicados)**: Utilize launchers de Kiosk industriais (como *Fully Kiosk Browser*) configurando a URL inicial para o endereço do servidor local.

---

## 🔌 Integração com a API RP Info
O servidor local consome os endpoints oficiais da **API RP Info v2.0.83**:
- **Autenticação**: `POST /v1.1/auth` (com renovação automática de token antes de expirar).
- **Consulta por Código de Barras**: `GET /v2.8/produtounidade/{codigoBarras}/unidade/{CNPJ}/consultarcodigobarras`.

---

## 📜 Licença & Autorização
Desenvolvido para uso operacional interno nos Supermercados Gmais.
