# Tag 00005 — Gerenciamento de serviços básicos referentes a unidade

4 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| GET | `/v1.0/unidades/extras/{cnpjOrCodigo}` | Lista os campos extras de uma unidade |  |
| GET | `/v1.0/unidades/simplificadas` | Listar unidades simplificadas |  |
| GET | `/v1.6/unidades` | retornar unidades |  |
| GET | `/v1.6/unidades/{CNPJ}` | retornar unidade |  |

## Detalhes

### GET `/v1.0/unidades/extras/{cnpjOrCodigo}`

**Resumo:** Lista os campos extras de uma unidade

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de autenticação |
| `cnpjOrCodigo` | path | sim | string | CNPJ ou Codigo da Unidade |

**Respostas:**

- `200` Requisição processada com sucesso — { response: object { status, appVersion, messages, content } }

---

### GET `/v1.0/unidades/simplificadas`

**Resumo:** Listar unidades simplificadas

Retorna somente o código e o nome das unidades, ordenadas pelo código, restritas às unidades liberadas para o usuário logado. Usuário sem restrição recebe todas.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de autenticação |

**Respostas:**

- `200` OK — **UnidadesSimplificadasResponseV_1_0** = object { response }

---

### GET `/v1.6/unidades`

**Resumo:** retornar unidades

retornar todas as unidades

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Respostas:**

- `200` retornar todos os dados de todas as unidades — **UnidadesResponseV_1_6** = object { response }

---

### GET `/v1.6/unidades/{CNPJ}`

**Resumo:** retornar unidade

retornar dados da unidade

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `CNPJ` | path | sim | string | CNPJ da unidade |

**Respostas:**

- `200` dados da unidade — **UnidadeResponseV_1_6** = object { response }

---
