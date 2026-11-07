# Tag 00025 — Cadastro de Cidades

3 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| POST | `/v1.1/cidades` | Cadastrar Cidade |  |
| GET | `/v1.2/cidades` | Buscar cidade por código interno ou código Ibge |  |
| GET | `/v1.2/cidades/{lastID}` | Buscar cidades cadastradas |  |

## Detalhes

### POST `/v1.1/cidades`

**Resumo:** Cadastrar Cidade

Dados da cidade a serem cadastrados

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **CadastrarCidade** = object { descricao, uf, codigoPais, codigoIBGE }

**Respostas:**

- `200` Cidade salva com sucesso — **RespostaCadastroCidade** = object { response }

---

### GET `/v1.2/cidades`

**Resumo:** Buscar cidade por código interno ou código Ibge

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | query | não | number | codigo interno |
| `codIbge` | query | não | number | codigo do Ibge |

**Respostas:**

- `200` Dados carregados com sucesso — **cadastroCidade** = object { response }

---

### GET `/v1.2/cidades/{lastID}`

**Resumo:** Buscar cidades cadastradas

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | string | Código da última cidade consultada. Envie "0" caso queira consultar todas as cidades (mesmo passando 0 os dados retornam paginados) |

**Respostas:**

- `200` Dados carregados com sucesso — **cadastroCidadeV2** = object { response }

---
