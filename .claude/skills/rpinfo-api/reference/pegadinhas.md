# Pegadinhas e aprendizados práticos — API RP Info

Coisas descobertas testando de verdade (scripts em `D:\Users\ti1gr\PycharmProjects\API-RP-INFO`),
que não ficam óbvias só lendo o spec. Atualizar sempre que um novo teste revelar algo.

## 1. `/v1.1/auth` está DEPRECIADO — use `/v1.1/auth` apenas como fallback

- O endpoint correto e atual é **`POST /v1.2/auth`** (tag `00001`, não depreciado).
- `POST /v1.1/auth` existe mas está na tag `00100` ("Serviços descontinuados") com `deprecated: true`.
- Os scripts legados do projeto (`Test-API.py`) ainda usam `/v1.1/auth`. Funciona, mas migrar para `/v1.2/auth` é o caminho recomendado pela própria doc da API.
- Payload de autenticação (igual nas duas versões): `{"usuario": "<codigo>", "senha": "<senha>"}`.
- `/v1.2/auth` aceita dois query params opcionais: `origem` (ex. `RPONEMOBILE`, `RPCOLLECT`) e `versao`.
- Resposta: `response.status` (`"ok"` ou erro), `response.token`, `response.tokenExpiration` (string `dd/MM/YYYY HH:mm:ss`), `response.expiresIn` (minutos).
- Logout: `GET /v1.1/logout` com header `token`.

### 1.2. Regra geral: sempre usar a versão ATUAL de cada endpoint, nunca a que "sempre foi usada"

- Descoberto ao revisar o exemplo do próprio `SKILL.md`: ele usava `/v1.9/movimentoprodutos/listarmovimentos/lastid/{lastId}`
  (igual aos scripts legados do cliente) mas **existe `/v2.0/` da mesma rota, e todo o `/v1.x/` está `deprecated: true`**.
  Ou seja, nem o próprio exemplo "oficial" desta skill estava na versão certa.
- Fix permanente: [`reference/versoes-atuais.md`](versoes-atuais.md) é **gerado automaticamente**
  (`python scripts/gerar_docs.py`, função `generate_versoes_atuais`) direto do campo `deprecated` de cada
  operação do spec — mapeia as 137 famílias de endpoint que existem em mais de uma versão e aponta qual é a
  atual. Consultar esse arquivo (ou regenerar) sempre que for usar/revisar um endpoint multi-versão, em vez
  de assumir que "a versão mais alta" ou "a que o script antigo usa" é a certa.
- **Pegadinha dentro da pegadinha:** número de versão mais alto **não é garantia** de ser o atual —
  existe pelo menos um caso real no spec (`DELETE /pedidos/{codigo}/item/{codigoItem}`) em que a `v1.9` está
  depreciada e a `v1.0` **não** está. O algoritmo de `versoes-atuais.md` já trata isso certo (só confia no
  campo `deprecated`, não assume ordem crescente), mas serve de alerta pra quem for conferir na mão.
- Seis famílias de endpoint ficaram com **todas as versões depreciadas** (nenhuma atual) — sinal de que a
  funcionalidade pode ter sido descontinuada/substituída por algo com nome diferente; `versoes-atuais.md`
  lista essas com `⚠️ todas depreciadas` e recomenda confirmar com a RP Info antes de tentar usar.

### 1.1. O spec muda com o tempo — não confiar em doc antiga sem reconferir

- Uma versão anterior desta mesma skill (gerada em jul/2026) documentava `/v1.1/auth` como o endpoint
  **recomendado**. No spec baixado em 2026-10-14, `/v1.1/auth` já está marcado `deprecated: true` (tag `00100`)
  e `/v1.2/auth` é o atual. Ou seja, a própria API RP Info mudou o que é "atual" entre essas datas.
- Lição: ao reusar qualquer nota antiga (inclusive deste arquivo), reconferir contra
  `openapi/rpinfo-openapi.yaml` baixado na data mais recente possível antes de confiar cegamente.

## 2. Endpoint `/v1.0/produtos/listar?produto=<codigo>` NÃO EXISTE

- `venv/Produto.py` tenta usar `GET /v1.0/produtos/listar?produto={codigo}` para pegar o `grupoNome` (departamento) de um produto, e **falha silenciosamente para 100% dos produtos** (sempre cai no `except` e grava `"Erro na Busca"` no CSV — ver `vendas_com_departamento.csv`).
- Esse path não existe no spec. O correto, **confirmado no schema** (`ConsultarCadastroProdutoResponse` → `response.produto` → `ProdutoCadastro`):
  - **`GET /v1.0/produto/{codigo}`** (tag `00004`) — path param, não query string.
  - O campo de departamento vem em **`response.produto.grupoNome`** (ex.: `"Carnes Bovinas De Primeira"`) e `response.produto.grupoCodigo` / `response.produto.departamentoCodigo`. Ou seja, o fix do `buscar_depto_produto()` legado é: trocar a URL para `f"http://192.168.1.4:9000/v1.0/produto/{codigo}"` (sem query `produto=`) e ler `dados["response"]["produto"]["grupoNome"]` em vez de `dados.get("response", {}).get("produto", {}).get("grupoNome")` num payload que nunca existiu.
  - Alternativa em lote (evita 1 request por produto): `GET /v1.9/produtounidade/listaprodutos/{lastID}/unidade/{CNPJ}/departamento/{departamento}` ou `.../detalhado/departamento/{departamento}` (filtra por departamento em vez de buscar o departamento de cada produto individualmente).
- **Lição geral:** antes de assumir que um endpoint "não tem o dado" ou "deu erro", confirmar o path exato em `reference/endpoints/` ou grepando `openapi/rpinfo-openapi.yaml` — o padrão de nomenclatura da API mistura singular/plural (`produto` vs `produtos`) de forma inconsistente entre tags.

## 2.1. Cache de resposta "Erro na Busca" é opaco — não silenciar exceptions

- O padrão `except: pass` / `return "Erro na Busca"` em `buscar_depto_produto()` esconde a causa real (404? timeout? token expirado?). Ao portar esses scripts, logar `response.status_code` e `response.text` no erro em vez de engolir a exceção.

## 3. Dois IPs diferentes na rede do cliente — não confundir

- **API RP Info (REST, porta 9000):** `192.168.1.4` (local) — é o que os scripts usam (`http://192.168.1.4:9000/...`).
- **Banco Postgres:** `192.168.1.10` — host separado, passado pelo usuário para a tarefa de conexão direta ao banco. Credenciais a confirmar.
- Servidor de homologação público da RP (fora da rede local): `http://servicosflex.rpinfo.com.br:9000` — é de onde a doc Swagger (`/v1.0/documentacao`) e o spec (`/v1.0/documentacao.yaml`) foram baixados.
- **Prioridade: API REST sempre em primeiro lugar.** Acesso direto ao Postgres é só pra caso extremo,
  quando a API não cobre o que é necessário — e, quando isso acontecer, avisar explicitamente que vai
  direto no banco e não pela API (nunca trocar silenciosamente).
- **Somente leitura, sempre** (API e banco) — nunca gravar/importar/alterar dado no banco do cliente.
- **Limite de conexões/requisições do banco: 1200** (informado pelo usuário em 2026-10-14) — cuidado pra
  não estourar: reusar/fechar conexões direito, não paralelizar sem controle.

## 4. Headers obrigatórios em toda chamada (exceto auth)

```
Content-Type: application/json
token: <token recebido em /v1.2/auth>
```

## 5. Paginação por `lastid` (não por página/offset)

- Padrão usado em endpoints de listagem incremental (`movimentoprodutos/listarmovimentos/lastid/{lastId}`, `produto/listaprodutos/{lastId}`, etc.): primeira chamada com `lastid=0`, pegar o maior `id` retornado no lote, usar como `lastid` da próxima chamada, repetir até vir lista vazia.
- Resposta pode vir em `dados["movimentos"]` **ou** `dados["response"]["movimentos"]` dependendo do endpoint/versão — sempre tratar os dois formatos (como já faz `Consulta-Vendas-Completo.py`).
- Pausa entre chamadas (`time.sleep(0.2)` no script legado) evita sobrecarregar a API em laços de paginação longos.

## 6. Erro 403 — formato `Response_Forbidden`

Quando o usuário autenticado não tem a permissão exigida pela rota:

```json
{
  "error": "Não Autorizado",
  "requiredPermission": {
    "httpMethod": "POST",
    "endpoint": "/v1.0/...",
    "enableAnyOf": [{"id": "...", "...": "..."}]
  }
}
```

- Basta habilitar **uma** das permissões em `enableAnyOf` no cadastro de usuários externos do ERP (no usuário ou em um grupo dele).
- `enableAnyOf` pode vir vazio se a permissão ainda não tem item correspondente cadastrado no ERP.
- Outras negativas (LGPD, bloqueio por força bruta, validações de negócio) trazem só `error`, sem `requiredPermission`.

## 7. Valores numéricos com ponto decimal — conversão pt-BR

- A API retorna decimais com ponto (`23.9`). Os scripts legados convertem para vírgula na hora de escrever CSV (`format_ptbr`). Útil manter esse padrão em qualquer exportação para Excel/PT-BR.

## 8. Datas em formato `dd-MM-yyyy` nos parâmetros de query

- Ex.: `datainicial=24-05-2026`, `datafinal=24-05-2026` (confirmado funcionando em `Consulta-Vendas.py`). Não é ISO (`yyyy-MM-dd`).

## 9. `/v1.2/auth` (e outros endpoints): payload real vem em `response.content`, não como o spec documenta

**Confirmado ao vivo em 2026-10-14** contra `http://192.168.1.4:9000` (ERP `appVersion: "5.0.7.022"`):

- O spec (schema `RespostaAutenticacao_V_1_1`, reaproveitado tanto pelo `/v1.1/auth` depreciado quanto
  pelo `/v1.2/auth` atual — é só o spec reciclando o nome, **não** significa que o v1.2 se comporta como
  v1.1) documenta a resposta de auth como:
  ```json
  {"response": {"status": "ok", "token": "...", "tokenExpiration": "...", "expiresIn": 3600}}
  ```
- A resposta **real** do servidor veio assim — com os dados de verdade dentro de `response.content`,
  e `status`/`appVersion`/`messages` soltos no nível de `response`:
  ```json
  {"response": {"status": "ok", "appVersion": "5.0.7.022", "messages": [...],
    "content": {"token": "...", "tokenExpiration": "2026-10-14T18:09:16.565Z", "expiresIn": 14400}}}
  ```
- **O mesmo padrão `response.content` apareceu também em `GET /v1.6/unidades`** (lista de lojas em
  `response.content`, não em `response.unidades`/raiz). Ou seja, isso não é só uma particularidade do
  `/auth` — parece um padrão real de envelope desta instalação/versão do ERP: `response.status` +
  `response.appVersion` + `response.messages` + `response.content` (o conteúdo de verdade sempre dentro
  de `content`, independente do nome que o spec dá pro campo específico do endpoint).
- `tokenExpiration` veio em **ISO 8601** (`2026-10-14T18:09:16.565Z`), não no formato
  `dd/MM/yyyy HH:mm:ss` que o spec descreve.
- `expiresIn` veio em **segundos** (`14400` = 4h, confirmado batendo com `iat`/`exp` do JWT decodificado),
  não em minutos como a descrição do schema diz ("Tempo em minutos para o token expirar"). **Não confiar
  cegamente na unidade documentada — se der pra conferir pela data absoluta (`tokenExpiration`), preferir
  isso a fazer conta com `expiresIn`.**
- `scripts/rp_auth.py` já foi corrigido para ler `response.content.token` com fallback pro formato plano
  documentado no spec (`response.token`), e para calcular expiração a partir de `tokenExpiration`
  (data absoluta) em vez de assumir a unidade de `expiresIn`.
- **Lição geral:** ao integrar um endpoint novo pela primeira vez, **testar com uma chamada real antes
  de confiar 100% no formato do spec** — o spec desta API já se mostrou desatualizado/divergente do
  comportamento real do servidor em produção (ver também item 1.1). Sempre imprimir o JSON bruto da
  primeira resposta real e conferir a forma antes de escrever o parser definitivo.

## 10. `response.content` muda de FORMA (dict ou lista) dependendo do endpoint — nunca assumir um só

**Confirmado ao vivo em 2026-10-14**, construindo o teste de round-trip do painel (`painel/app.py`,
aba "Endpoint de Negócio") contra `GET /v1.6/unidades`:

- Em `/v1.2/auth`, `response.content` é um **objeto/dict** (`{"token": "...", "tokenExpiration": "...", ...}`).
- Em `GET /v1.6/unidades`, `response.content` é uma **lista** de objetos (`[{"codigo": "001", "nome": "...", ...}, ...]`)
  — bate com o schema do spec (`UnidadesResponseV_1_6.response.content: array`), então aqui o spec estava certo;
  o perigo é só escrever um parser genérico assumindo que `content` é sempre dict (como em `/auth`).
- **Bug real cometido e corrigido nesta sessão:** um parser que fazia
  `content = response.get("content") if isinstance(response.get("content"), dict) else response`
  (pensado olhando só pro formato do `/auth`) falhava silenciosamente em `/v1.6/unidades`: como
  `content` ali é lista (não dict), caía no fallback `content = response` inteiro, e ao procurar "a
  primeira lista dentro do dict" (`next(v for v in content.values() if isinstance(v, list))`) pegava
  `response.messages` (lista com só `{"message": "Requisição processada com sucesso"}`) em vez da
  lista de verdade em `response.content` — porque `messages` aparece antes de `content` na ordem das
  chaves do JSON. O teste "funcionava" (200 OK, token válido) mas devolvia **dado errado**, sem erro
  nenhum pra avisar.
- **Como evitar:** ao escrever um parser para `response.content`, checar o **tipo** primeiro
  (`isinstance(content, list)` vs `isinstance(content, dict)`) antes de decidir onde buscar os dados —
  nunca varrer genericamente "a primeira lista encontrada em `response`", porque `response.messages`
  quase sempre existe e quase sempre é uma lista (ainda que só com texto de confirmação), e um scan
  genérico pega ela por engano. Ver implementação corrigida em `painel/app.py` (`testar_endpoint_negocio`).

## 11. `/v1.0/produtounidade/ofertas` não traz data inicial/final da oferta — só se está em oferta ou não

**Confirmado ao vivo em 2026-10-14**, testando a aba "Ofertas por Loja" do painel contra o ambiente do
cliente (uma loja real, identificada só pelo código de unidade `001` aqui — CNPJ omitido de propósito):

- `GET /v1.0/produtounidade/ofertas` (o endpoint certo/atual pra listar ofertas vigentes — ver seção
  acima) **não tem campo de data** no schema nem na resposta real: só `precoAnterior`/`precoAtual` e
  dados do produto. Ele diz **que** um produto está em oferta (porque apareceu na lista) e **qual** o
  preço, mas não diz **desde quando** nem **até quando** essa oferta vale.
- Existe uma família de endpoints separada — "agenda de ofertas" (`GET
  /v1.3/agendas/periodoInicio/unidade/{cnpj}/lastid/{lastId}`, `/v1.3/agendas/periodoFinal/...` e
  `/v1.3/agendas/datainicio/{dataInicio}/datafim/{dataFim}/unidade/{cnpj}/lastid/{lastId}`, tag `00008`,
  v1.3 é a versão atual — ver `reference/versoes-atuais.md`) — cujo schema **tem** `DataInicio`/`DataFim`
  tanto no nível da agenda quanto (opcionalmente) por produto dentro dela.
- **Mas, testado ao vivo paginando por `lastId`** (loja 001, de `lastId=0` até esgotar), **a última
  agenda cadastrada neste cliente é de 28/11/2023 a 01/12/2023** (`Codigo=52910030`) — não existe
  nenhuma agenda com data posterior a dez/2023, mesmo a API estando em produção até hoje (2026-10-14).
  **Confirmado pelo usuário** (não é só suposição a partir do teste): esse recurso de "agenda de
  ofertas" é o mecanismo **antigo**, e o sistema **migrou** pro mecanismo atual, que é exatamente
  `/v1.0/produtounidade/ofertas` (o que já está implementado na aba "Ofertas por Loja" do painel) —
  **não tem, hoje, nenhuma via confirmada da API pra pegar a data de início/fim de uma oferta
  atualmente vigente neste cliente**, porque o mecanismo novo simplesmente não guarda essa data.
- **Antes de assumir que vale pro seu ambiente:** se for outro cliente/instalação, vale testar se o
  recurso de agenda ainda está em uso lá (paginar `/v1.3/agendas/periodoInicio/unidade/{cnpj}/lastid/0`
  até o fim e ver a data do último registro) antes de concluir que a data não está disponível.
- Reparo de schema (bônus, mesmo teste): a resposta real usa `produtos` (minúsculo) e `Obervacao` (sem o
  "s" de "Observação" — erro de digitação no nome do campo da API), enquanto o spec documenta
  `Produtos`/`Observacao`. Mais um caso da "Regra de ouro": nunca confiar 100% no nome exato de campo do
  spec sem testar ao vivo.
