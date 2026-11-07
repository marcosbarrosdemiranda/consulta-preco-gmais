---
name: rpinfo-api
description: Especialista na API REST da RP Info (sistemas RP One, Flex, Mix, Cxo e Mix-Integração) — autenticação por token, 683 endpoints (produtos, clientes, vendas, estoque, financeiro, fiscal, compras, etc.), paginação por lastid, e integração direta com o banco Postgres do ERP. Use sempre que o usuário mencionar RP Info, RP Services, Flex/Mix/Cxo, sistema de PDV ou automação comercial, perguntar sobre endpoints da RP Info, construir/depurar scripts de integração (vendas, produtos, movimentos de estoque), diagnosticar erros de autenticação/permissão (403, token) contra essa API, ou conectar no banco Postgres do sistema.
---

# API RP Info — referência do especialista

API REST que expõe regras de negócio dos sistemas **RP One, Flex, Mix, Cxo e Mix-Integração**
(retaguarda de varejo: produtos, vendas, estoque, financeiro, fiscal, compras, clientes, RH, etc.).

- Spec oficial (OpenAPI 3.0.1) baixado de `http://servicosflex.rpinfo.com.br:9000/v1.0/documentacao` em 2026-10-14,
  salvo integralmente em [`openapi/rpinfo-openapi.yaml`](openapi/rpinfo-openapi.yaml) (2,4 MB, 683 endpoints, 859 schemas).
- Documentação navegável gerada a partir do spec: [`reference/_index.md`](reference/_index.md) → por tag em `reference/endpoints/*.md`.
- **Qual versão usar por endpoint** (gerado automaticamente do spec, 137 famílias multi-versão mapeadas): [`reference/versoes-atuais.md`](reference/versoes-atuais.md) — **SEMPRE consultar antes de usar um endpoint que existe em várias versões** (`/v1.0/`, `/v1.1/`... `/v2.0/`...); a versão mais alta nem sempre é a atual (tem caso real em que uma versão mais nova foi depreciada e uma mais antiga voltou a ser a vigente).
- Dicionário de schemas: [`reference/schemas.md`](reference/schemas.md).
- Schema real do banco Postgres do cliente (tabelas, colunas, PKs/FKs, mapeado ao vivo, somente leitura):
  [`reference/db-schema/_index.md`](reference/db-schema/_index.md) → `erp.md` (91 tabelas, banco principal
  do ERP), `vdadet.md` (158 tabelas), `wrpdv.md` (só views de sistema, sem tabela de aplicação). Gerado por
  `scripts/mapear_banco.py` — **nunca** contém usuário/senha, só metadado de estrutura.
- Armadilhas e aprendizados de uso real (scripts testados contra o ambiente do cliente): [`reference/pegadinhas.md`](reference/pegadinhas.md) — **ler antes de escrever qualquer integração nova**.
- Painel de testes web local, **opcional** (não necessário pra skill funcionar): [`painel/`](painel/README.md),
  documentado em [`reference/painel-de-testes.md`](reference/painel-de-testes.md).

> Como a doc por tag é gerada automaticamente e é grande, **não leia todos os arquivos de uma vez**: comece por este SKILL.md,
> depois abra só o arquivo de tag relevante (`reference/_index.md` tem a lista com contagem de endpoints), e grepe
> `openapi/rpinfo-openapi.yaml` para o detalhe bruto de um schema/endpoint específico quando precisar de algo que o
> resumo gerado simplificou.

## Prioridade de acesso: API REST sempre primeiro, banco direto é última instância

- **Padrão: resolver qualquer necessidade de dados pela API REST.** Acesso direto ao banco Postgres do
  ERP (quando disponível/configurado) é **exceção, caso extremo** — só quando a API comprovadamente não
  cobre o que é preciso (nenhum endpoint, nem combinando vários, entrega aquele dado/relatório).
- **Nunca usar banco direto no lugar da API sem avisar antes, de forma clara e explícita, que não vai
  usar a API e sim o banco diretamente.** Isso vale tanto ao propor uma abordagem quanto ao executá-la.
- **Somente leitura, sempre — tanto pela API quanto pelo banco.** Nunca gravar/importar/alterar dado
  nenhum no banco do cliente (sem `INSERT`/`UPDATE`/`DELETE`/DDL) nem usar a API para escrever dados sem
  pedido explícito do usuário para aquela operação específica. Só consulta.
- **Cuidado com o limite de conexões/requisições do banco (1200, confirmar se mudou)** ao fazer acesso
  direto ao Postgres — evitar abrir conexões em excesso ou paralelizar sem controle.

## Ambientes conhecidos

| Ambiente | Host | Observação |
|---|---|---|
| Homologação/documentação pública RP | `http://servicosflex.rpinfo.com.br:9000` | de onde a doc/spec foi baixada; serve para testes e consulta do Swagger |
| API do cliente (rede local) | `http://192.168.1.4:9000` | usado nos scripts reais em `D:\Users\ti1gr\PycharmProjects\API-RP-INFO` |
| Banco Postgres do cliente | `192.168.1.10` | **tarefa pendente**: testar conexão direta; credenciais a confirmar com o usuário |

Todos os hosts usam a mesma estrutura de rotas (`/v{versão}/recurso`); só muda o host base.

## Autenticação

1. `POST /v1.2/auth` (tag `00001` — **endpoint atual, não depreciado**; ver [`reference/pegadinhas.md`](reference/pegadinhas.md#1-v11auth-está-depreciado--use-v11auth-apenas-como-fallback) sobre `/v1.1/auth` depreciado) com body:
   ```json
   { "usuario": "<codigo do usuário>", "senha": "<senha>" }
   ```
   Query params opcionais: `origem` (`RPONEMOBILE`, `RPCOLLECT`), `versao`.
2. Resposta (`response.status == "ok"`): o spec documenta `response.token`/`response.tokenExpiration`/`response.expiresIn`
   direto, mas **confirmado ao vivo** (2026-10-14) o servidor real aninha em `response.content.token` /
   `response.content.tokenExpiration` (ISO 8601) / `response.content.expiresIn` (em **segundos**, não minutos —
   ver [`reference/pegadinhas.md`](reference/pegadinhas.md#9-v12auth-e-outros-endpoints-payload-real-vem-em-responsecontent-não-como-o-spec-documenta)).
   `scripts/rp_auth.py` já trata os dois formatos. Guardar o token — ele deve ser reenviado em **todas** as chamadas seguintes.
3. Toda requisição (exceto auth) precisa dos headers:
   ```
   Content-Type: application/json
   token: <token recebido>
   ```
4. Logout: `GET /v1.1/logout` com header `token`.
5. 403 por falta de permissão → corpo no formato `Response_Forbidden` (`error` + `requiredPermission.enableAnyOf`). Ver detalhe em [`reference/pegadinhas.md`](reference/pegadinhas.md#6-erro-403--formato-response_forbidden).

Script pronto para autenticar sem escrever código na hora: [`scripts/rp_auth.py`](scripts/rp_auth.py)
(lê usuário/senha/host de variáveis de ambiente ou `--usuario`/`--senha`/`--host`, nunca hardcoded; salva o
token em `rp_token.json` local com controle de expiração — `--show` / `--check`).

### Diagnóstico rápido de erro

| Sintoma | Causa provável |
|---|---|
| 401 | Token inválido/expirado → reautenticar (`POST /v1.2/auth`) |
| 403 com `requiredPermission` | Falta permissão específica do endpoint — habilitar uma de `enableAnyOf` no cadastro do usuário externo |
| 403 só com `error` (sem `requiredPermission`) | Regra de negócio, LGPD ou bloqueio por força bruta — não é permissão de endpoint |
| 404 | Conferir se o path é exatamente o do spec — a API mistura singular/plural (`produto` vs `produtos`) de forma inconsistente entre tags, fácil de errar (ver [`reference/pegadinhas.md`](reference/pegadinhas.md) item 2) |
| Request "falha" sem exceção clara / corpo vazio | Checar se o endpoint não está **depreciado** ou se o path simplesmente não existe — endpoint inexistente costuma responder 404 de rota (framework), não um erro de negócio |
| Campo sempre vazio/zerado mesmo com request OK | Conferir se não é caso de resposta aninhada (`response.produto...` ou `response.content...` vs raiz) — ver convenção abaixo |

## Convenções gerais da API

- **Paginação incremental por `lastid`** (não por página): endpoints de listagem em massa (produtos, movimentos, clientes) recebem `.../lastid/{lastId}` na URL; pegar o maior `id` do lote e repetir até vir lista vazia. Detalhe em [`reference/pegadinhas.md`](reference/pegadinhas.md#5-paginação-por-lastid-não-por-páginaoffset).
- **Resposta aninhada inconsistente**: alguns endpoints devolvem a lista direto na raiz (`{"movimentos": [...]}`), outros dentro de `{"response": {"movimentos": [...]}}`, e **confirmado ao vivo** que em pelo menos dois endpoints (`/v1.2/auth`, `/v1.6/unidades`) o dado real fica em `response.content` — mesmo quando o spec documenta outro nome de campo. Sempre tratar múltiplos formatos e, ao integrar endpoint novo, testar com uma chamada real antes de confiar no spec (ver [`reference/pegadinhas.md`](reference/pegadinhas.md) item 9).
- **`response.content` não tem forma fixa**: pode ser um objeto (`/v1.2/auth`) ou uma lista (`/v1.6/unidades`), dependendo do endpoint. Ao escrever um parser, checar o **tipo** de `content` antes de decidir onde buscar o dado — nunca varrer genericamente "a primeira lista dentro de `response`", porque `response.messages` quase sempre existe e é lista, e um scan genérico cai nela por engano (ver [`reference/pegadinhas.md`](reference/pegadinhas.md) item 10).
- **Datas em parâmetros de query**: formato `dd-MM-yyyy` (ex.: `datainicial=24-05-2026`), não ISO.
- **Decimais**: a API retorna com ponto (`23.9`); conversão para vírgula é responsabilidade do consumidor (padrão pt-BR já usado nos scripts legados).
- **Content-Type obrigatório**: `application/json` em todo método.
- Parâmetros devem ser `URL-encoded`.
- Multi-versão: a mesma funcionalidade costuma existir em várias versões de path (`/v1.0/`, `/v1.1/`, ..., `/v2.8/`...). **Sempre usar a versão atual, nunca fixar de cor numa versão vista antes** — consultar [`reference/versoes-atuais.md`](reference/versoes-atuais.md) (gerado automaticamente a partir do campo `deprecated` do spec) ou a coluna "Depreciado" da lista rápida de cada arquivo em `reference/endpoints/`. Tag `00100` ("Serviços descontinuados") agrupa só depreciados.

## Mapa de tags (categorias) mais usadas

Lista completa com contagem de endpoints em [`reference/_index.md`](reference/_index.md). Destaques:

| Tag | Assunto | Arquivo |
|---|---|---|
| 00001 | Autenticação de sessão | `reference/endpoints/00001-autenticacao-de-sessao.md` |
| 00002 | Autenticação de cadastros | `reference/endpoints/00002-*.md` |
| 00003 | Serviços básicos dos clientes | `reference/endpoints/00003-*.md` |
| 00004 | Serviços básicos dos produtos | `reference/endpoints/00004-*.md` |
| 00008 | Movimento de produtos (vendas/estoque) | `reference/endpoints/00008-*.md` |
| 00009 | Movimento referente a clientes | `reference/endpoints/00009-*.md` |
| 00010 | Movimento de estoque | `reference/endpoints/00010-*.md` |
| 00011 | Venda | `reference/endpoints/00011-*.md` |
| 00012 | Compra | `reference/endpoints/00012-*.md` |
| 00017 | Dados financeiros | `reference/endpoints/00017-*.md` |
| 00027 | Fiscal | `reference/endpoints/00027-*.md` |
| 00100 | Serviços descontinuados (NÃO usar em código novo) | `reference/endpoints/00100-*.md` |

## Exemplo rápido (Python)

```python
import requests

HOST = "http://192.168.1.4:9000"  # ou o host do ambiente em questão

auth = requests.post(f"{HOST}/v1.2/auth", json={"usuario": "<usuario>", "senha": "<senha>"},
                      headers={"Content-Type": "application/json"}).json()
token = auth["response"]["token"]
headers = {"token": token, "Content-Type": "application/json"}

# Paginação por lastid (v2.0 é a atual; ver reference/versoes-atuais.md antes de fixar uma versão)
last_id, todos = 0, []
while True:
    r = requests.get(f"{HOST}/v2.0/movimentoprodutos/listarmovimentos/lastid/{last_id}",
                      params={"unidade": "001", "datainicial": "24-05-2026", "datafinal": "24-05-2026"},
                      headers=headers, timeout=60).json()
    lote = r.get("movimentos") or r.get("response", {}).get("movimentos", []) if isinstance(r, dict) else r
    if not lote:
        break
    todos.extend(lote)
    last_id = max(item.get("id", 0) for item in lote)
```

## Painel de testes (ferramenta opcional)

A skill inclui, em [`painel/`](painel/README.md), um painel web local **opcional** pra testar a API (e,
se configurado, o Postgres direto) num navegador em vez de ler log/JSON cru — útil pra confirmar um
achado de `pegadinhas.md` com uma chamada real antes de documentar. Não é necessário pra skill
funcionar; tudo via `.env` próprio (`painel/.env.example`), credencial nunca hardcoded. Ver
[`reference/painel-de-testes.md`](reference/painel-de-testes.md) para detalhes, e
`painel/README.md` para o passo a passo de instalação.

## Suíte de evals

[`evals/evals.json`](evals/evals.json) — casos de teste da skill (auth, paginação, diagnóstico de 403,
endpoint inexistente). Usar com a ferramenta de eval de skills do Claude Code para validar mudanças aqui.

## Código real existente (ponto de partida)

Scripts de teste/produção já escritos pelo usuário em `D:\Users\ti1gr\PycharmProjects\API-RP-INFO`
(Python + `requests`, venv próprio já criado):

| Arquivo | O que faz |
|---|---|
| `Test-API.py` | Teste simples de `POST /v1.1/auth` (usar `/v1.2/auth` em código novo) |
| `Consulta-Vendas.py` | Extrai movimentos de produtos de um dia (`/v1.9/movimentoprodutos/listarmovimentos/lastid/0`) e gera CSV pt-BR |
| `Consulta-Vendas-Completo.py` | Mesma ideia + paginação completa por `lastid` + filtro por `tipoDcto` (`EVA/EVD/EVL/EVP`) |
| `venv/Produto.py` | Cruza movimento com departamento do produto — **tem bug conhecido**, ver [`reference/pegadinhas.md`](reference/pegadinhas.md#2-endpoint-v10produtoslistarprodutocodigo-não-existe) |

Esses scripts contêm usuário/senha e tokens JWT **em texto plano** — nunca reescrever/colar esses valores em arquivos da skill ou em respostas; tratar como segredo do cliente.

**Convenção de credenciais:** como esta skill é copiada/instalada em várias máquinas e usada por usuários diferentes, credenciais de teste (usuário/senha da API, string de conexão do Postgres) **nunca vão em arquivos desta skill nem em código versionado**. Cada máquina guarda as suas próprias num arquivo local não versionado (ex.: `.env` na raiz do projeto, fora de `.claude/skills/`, listado no `.gitignore`).

## Como gerar/atualizar esta documentação

O conteúdo de `reference/` e `openapi/rpinfo-openapi.yaml` é gerado por
[`../../../scripts/gerar_docs.py`](../../../scripts/gerar_docs.py) a partir do spec baixado. Para atualizar:

1. Baixar de novo: `curl -o openapi/rpinfo-openapi.yaml http://servicosflex.rpinfo.com.br:9000/v1.0/documentacao.yaml`
   (⚠️ é HTTP puro, não HTTPS — o servidor não responde em TLS nessa porta).
2. Rodar `python scripts/gerar_docs.py` a partir da raiz do projeto (`C:\Claude Code\API RP INFO`).

## Próximas tarefas deste projeto

1. ~~Baixar e organizar a documentação da API~~ ✅ feito.
2. **Testar conexão com o Postgres do cliente em `192.168.1.10`** — aguardando credenciais (usuário/senha/porta/nome do banco) que o usuário vai passar.
3. Mapear quais dados fazem mais sentido vir direto do Postgres vs. via API REST (a API já cobre a maior parte dos relatórios que os scripts legados tentam montar manualmente).
