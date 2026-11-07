# Painel de testes (opcional)

Ferramenta local que acompanha a skill — **não é necessária pra ela funcionar**, é só um atalho
visual pra quem quiser testar/explorar a API (e opcionalmente o Postgres) num navegador em vez
de ler log/JSON cru. Funciona com qualquer instalação da RP Info: todo endereço/credencial vem
do seu próprio `.env`, nada fica hardcoded aqui.

Reaproveita a autenticação já corrigida de `../scripts/rp_auth.py` (ver
`../reference/pegadinhas.md` item 9 — `response.content`, `expiresIn` em segundos, etc.), em
vez de duplicar essa lógica.

## Abas

- **Conexão API-Banco** — dois testes independentes (API sempre em primeiro lugar, banco direto
  é última instância — ver "Prioridade de acesso" no `CLAUDE.md`/`SKILL.md` do projeto onde isto
  for usado; aqui o objetivo é só diagnóstico/visualização):
  - **API REST**: `POST /v1.2/auth` — autentica e mostra host/usuário/token mascarado/validade.
  - **Postgres (direto)**: conecta num dos bancos listados em `RPINFO_DB_BANCOS` (`.env`) e roda
    só `SELECT version()`. Se `RPINFO_DB_BANCOS` estiver vazio, esta aba fica desabilitada — é o
    padrão seguro pra uma instalação nova, já que a API é sempre a via preferida.
- **Endpoint de Negócio** — round-trip completo: autentica, pega o token e chama
  `GET /v1.6/unidades` (endpoint de negócio real, somente leitura) pra confirmar que o token
  funciona ponta a ponta, não só a autenticação isolada.
- **Ofertas por Loja** — escolhe uma loja (lista buscada ao vivo em `/v1.6/unidades`, nunca
  fixa/hardcoded) e busca as ofertas de preço vigentes via
  `GET /v1.0/produtounidade/ofertas` (tag `00004`, atual — confirmado ao vivo em 2026-10-14,
  bate com o spec). Pagina por `lastId` (= maior `codigoProduto` do lote anterior, até 10
  páginas de 1000 itens por segurança) e mostra a lista inteira numa tabela (produto, marca,
  preço anterior/atual, código de barras). Filtros opcionais de departamento/setor.
  **Não mostra data inicial/final da oferta** porque esse endpoint não tem esse campo — ver
  `../reference/pegadinhas.md` item 11 (existe uma "agenda de ofertas" separada com datas no schema,
  mas é um mecanismo antigo que costuma já ter sido substituído pelo atual — confirmar caso a caso
  por instalação, paginando até o fim, antes de assumir que a data está disponível ali).
- **Histórico** — todos os testes já rodados (qualquer aba), com data/hora, categoria, subtipo
  e status. Botão **"Gerar achado"** por linha: monta um rascunho de texto no formato de
  `reference/pegadinhas.md` a partir daquele teste — só rascunho, **nunca escreve sozinho** no
  arquivo da skill; revisar/editar e colar manualmente se valer a pena documentar.

## Como rodar

```powershell
cd painel
copy .env.example .env   # preencher com os dados DA SUA instalação RP Info
pip install -r requirements.txt
python app.py
```

Abre em **http://127.0.0.1:5000** — só nesta máquina (`host=127.0.0.1`), não expõe na rede.

## Configuração (`.env`)

Ver `.env.example` pros nomes exatos de cada variável. Resumo:

| Variável | Obrigatória | Pra quê |
|---|---|---|
| `RPINFO_API_BASE_URL`, `RPINFO_API_USUARIO`, `RPINFO_API_SENHA` | sim | abas API/Negócio/Ofertas |
| `RPINFO_DB_HOST`, `RPINFO_DB_PORT`, `RPINFO_DB_USER`, `RPINFO_DB_PASSWORD` | não | aba de banco direto |
| `RPINFO_DB_BANCOS` | não | lista (separada por vírgula) dos bancos que o seletor pode mostrar; vazio = aba desabilitada |

## Armazenamento

Cada teste clicado é salvo em `painel/historico.db` (SQLite, **local e nunca versionado**).
Guarda só o que cada teste já retorna (ver regras abaixo), nunca senha/token em texto puro.

## Regras de segurança

- **Credenciais só vêm do `.env`** (nunca hardcoded aqui, nunca devolvidas inteiras ao navegador
  nem salvas no histórico — token e senha sempre mascarados/omitidos antes de qualquer
  retorno/gravação).
- **Somente leitura em tudo**: o teste de API só autentica; o teste de endpoint de negócio e o
  de ofertas só fazem `GET` em endpoints de listagem; o teste de banco só roda
  `SELECT version()`/`SELECT current_database()`.
- **Banco é lista fechada** pelo `RPINFO_DB_BANCOS` do `.env`: o navegador escolhe só entre o que
  está nessa lista, nunca manda nome de banco livre pro backend.
- **Uma tentativa só por clique**, com os parâmetros exatos do `.env` — nunca adivinha variação
  de credencial/parâmetro.
- O rascunho de "Gerar achado" pode incluir dados reais do teste (ex.: dados de lojas/produtos
  do ambiente testado) — revisar e tirar qualquer coisa sensível antes de colar em
  `pegadinhas.md`/commitar em qualquer repositório.
- Roda com o servidor de desenvolvimento do Flask (`debug=False`), só para uso local — não é
  pensado pra produção/exposição externa.
