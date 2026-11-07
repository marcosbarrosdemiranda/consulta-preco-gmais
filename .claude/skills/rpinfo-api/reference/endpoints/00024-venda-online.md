# Tag 00024 — Venda Online

4 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| GET | `/v1.0/vdonline/pdvs/unidade/{cnpj}/lastid/{lastid}` | Buscar PDVs da Unidade |  |
| GET | `/v1.0/vdonline/quantidade` | Busca a quantidade vendida de um produto |  |
| GET | `/v1.3/vdonlinefi/lastid/{lastId}` | Buscar vendas online Fi |  |
| GET | `/v1.5/vdonline/lastid/{lastId}` | Buscar vendas online |  |

## Detalhes

### GET `/v1.0/vdonline/pdvs/unidade/{cnpj}/lastid/{lastid}`

**Resumo:** Buscar PDVs da Unidade

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `cnpj` | path | sim | string |  |
| `lastid` | path | sim | string | Código do último PDV consultado. Envie "0" caso queira consultar todos os PDVs  (mesmo passando 0 os dados retornam paginados) |

**Respostas:**

- `200` Dados carregados com sucesso — **vdonlineUndPdv** = object { response }

---

### GET `/v1.0/vdonline/quantidade`

**Resumo:** Busca a quantidade vendida de um produto

Busca a quantidade vendida de um produto de um dia em uma unidade

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de autenticação |
| `unidade` | query | sim | string | CNPJ ou código da unidade |
| `produto` | query | sim | number | Código do produto |
| `data` | query | sim | string | Data de movimento (Formato "dd-mm-yyyy") |

**Respostas:**

- `200` Requisição processada com sucesso — { response: object { status, appVersion, messages, content } }

---

### GET `/v1.3/vdonlinefi/lastid/{lastId}`

**Resumo:** Buscar vendas online Fi

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de autenticação |
| `unidade` | query | sim | string | CNPJ ou código da unidade |
| `datainicial` | query | sim | string | Data inicial da venda (Formato "dd-mm-yyyy") |
| `datafinal` | query | sim | string | Data final da venda |
| `pdv` | query | não | string | Código do PDV |
| `cnpjCpf` | query | não | string | Cnpj ou Cpf do cliente do cupom de venda |
| `cnpjCpfCrm` | query | não | string | Cnpj ou Cpf do cliente do CRM de venda |
| `lastId` |  | não |  |  |

**Respostas:**

- `200` Dados carregados com sucesso — **vdonlineVdPdvFi_V_1_3** = object { response }

---

### GET `/v1.5/vdonline/lastid/{lastId}`

**Resumo:** Buscar vendas online

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de autenticação |
| `unidade` | query | sim | string | CNPJ ou código da unidade |
| `datainicial` | query | sim | string | Data inicial da venda (Formato "dd-mm-yyyy") |
| `datafinal` | query | sim | string | Data final da venda |
| `pdv` | query | não | string | Código do PDV |
| `cnpjCpf` | query | não | string | Cnpj ou Cpf do cliente do cupom de venda |
| `cnpjCpfCrm` | query | não | string | Cnpj ou Cpf do cliente do CRM de venda |
| `lastId` |  | não |  |  |

**Respostas:**

- `200` Dados carregados com sucesso — **vdonlineVdPdv_V_1_5** = object { response }

---
