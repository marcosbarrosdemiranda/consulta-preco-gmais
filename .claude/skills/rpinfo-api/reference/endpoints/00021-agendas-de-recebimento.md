# Tag 00021 — Agendas de Recebimento

2 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| GET | `/v1.0/agrec/fornecedor/{cnpjForn}/unidade/{cnpjUnid}` | Agendas de recebimento vigentes |  |
| GET | `/v1.1/agrec/fornecedor/{cnpjForn}/unidade/{cnpjUnid}` | Agendas de recebimento vigentes |  |

## Detalhes

### GET `/v1.0/agrec/fornecedor/{cnpjForn}/unidade/{cnpjUnid}`

**Resumo:** Agendas de recebimento vigentes

Busca de agendas de recebimento vigentes.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cnpjForn` | path | sim | string | CNPJ do fornecedor a consultar |
| `cnpjUnid` | path | sim | string | CNPJ da unidade a consultar |

**Respostas:**

- `200` Dados carregados com sucesso — **ListaAgendas** = object { response }

---

### GET `/v1.1/agrec/fornecedor/{cnpjForn}/unidade/{cnpjUnid}`

**Resumo:** Agendas de recebimento vigentes

Busca de agendas de recebimento vigentes com filtro de datas.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de autenticação |
| `cnpjForn` | path | sim | string | CNPJ do fornecedor a consultar |
| `cnpjUnid` | path | sim | string | CNPJ ou Código da unidade a consultar |
| `status` | query | não | string | Status do agendamento. |
| `dataAgInicial` | query | não | string | Data inicial do período de agendamento. Deve ser usada em conjunto com `dataAgFinal`. (Formato 'dd-MM-yyyy') |
| `dataAgFinal` | query | não | string | Data final do período de agendamento. Deve ser usada em conjunto com `dataAgInicial`. (Formato 'dd-MM-yyyy') |
| `dataCancInicial` | query | não | string | Data inicial do período de cancelamento. Deve ser usada em conjunto com `dataCancFinal`. (Formato 'dd-MM-yyyy') |
| `dataCancFinal` | query | não | string | Data final do período de cancelamento. Deve ser usada em conjunto com `dataCancInicial`. (Formato 'dd-MM-yyyy') |
| `dataEfetInicial` | query | não | string | Data inicial do período de efetivação da agenda. Deve ser usada em conjunto com `dataEfetFinal`. (Formato 'dd-MM-yyyy') |
| `dataEfetFinal` | query | não | string | Data final do período de efetivação da agenda. Deve ser usada em conjunto com `dataEfetInicial`. (Formato 'dd-MM-yyyy') |
| `dataConfFornInicial` | query | não | string | Data inicial da confirmação do agendamento com o fornecedor. Deve ser usada em conjunto com `dataConfFornFinal`. (Formato 'dd-MM-yyyy') |
| `dataConfFornFinal` | query | não | string | Data final da confirmação do agendamento com o fornecedor. Deve ser usada em conjunto com `dataConfFornInicial`. (Formato 'dd-MM-yyyy') |

**Respostas:**

- `200` Dados carregados com sucesso — **ListaAgendas** = object { response }

---
