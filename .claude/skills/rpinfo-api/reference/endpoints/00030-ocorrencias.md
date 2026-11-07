# Tag 00030 — Ocorrências

2 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| GET | `/v1.0/ocorrencias/pendentes/unidade/{cnpjUnid}/catentidade/{catentidade}/codentidade/{codentidade}` | Ocorrências pendentes da entidade |  |
| GET | `/v1.0/ocorrencias/unidade/{cnpjUnid}/catentidade/{catentidade}/codentidade/{codentidade}` | Ocorrências da entidade |  |

## Detalhes

### GET `/v1.0/ocorrencias/pendentes/unidade/{cnpjUnid}/catentidade/{catentidade}/codentidade/{codentidade}`

**Resumo:** Ocorrências pendentes da entidade

Busca as ocorrencias pendentes da entidade durante o último ano

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cnpjUnid` | path | sim | string | CNPJ da unidade a consultar |
| `catentidade` | path | sim | string | Categoria da entidade a consultar. Valores válidos: F;U;C;N; (Fornecedor;Unidade;Cliente;Nenhuma) |
| `codentidade` | path | sim | string | Código da entidade a consultar |

**Respostas:**

- `200` Dados caregados — **OcorrenciasEntidadeResponseV1** = object { response }

---

### GET `/v1.0/ocorrencias/unidade/{cnpjUnid}/catentidade/{catentidade}/codentidade/{codentidade}`

**Resumo:** Ocorrências da entidade

Busca as ocorrencias da entidade durante o último ano

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cnpjUnid` | path | sim | string | CNPJ da unidade a consultar |
| `catentidade` | path | sim | string | Categoria da entidade a consultar. Valores válidos: F;U;C;N; (Fornecedor;Unidade;Cliente;Nenhuma) |
| `codentidade` | path | sim | string | Código da entidade a consultar |

**Respostas:**

- `200` Dados caregados — **OcorrenciasEntidadeResponseV1** = object { response }

---
