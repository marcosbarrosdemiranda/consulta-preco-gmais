# Tag 00044 — Contas

2 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| GET | `/v1.0/subcontas` | Consultar o cadastro de sub contas |  |
| GET | `/v1.0/subcontas/movimentos` | Consultar os movimentos de sub contas |  |

## Detalhes

### GET `/v1.0/subcontas`

**Resumo:** Consultar o cadastro de sub contas

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Respostas:**

- `200` Requisição processada com sucesso — **ConsultaSubContasV1_0** = object { response }

---

### GET `/v1.0/subcontas/movimentos`

**Resumo:** Consultar os movimentos de sub contas

Consultar os movimentos de sub contas, filtrando por unidade, código de sub conta e **release OU data**.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `unidade` | query | não | string | Código da unidade ou cnpj a ser usado como filtro |
| `subConta` | query | não | string | Código da sub conta a ser usado como filtro |
| `release` | query | não | integer | Identificador do último fornecedor consultado. Utilize **0** para retornar todos os fornecedores (nesse caso os resultados serão sempre paginados). Para aplicar o filtro por `release`, os parâmetros `dataFinal` e `dataInicial` não devem ser informados. |
| `dataInicial` | query | não | string | Data Inicial a ser usado como filtro. Deve ser usada em conjunto com `dataFinal`. (Formato 'dd-MM-yyyy') |
| `dataFinal` | query | não | string | Data final a ser usado como filtro. Deve ser usada em conjunto com `dataInicial`. (Formato 'dd-MM-yyyy') |

**Respostas:**

- `200` Requisição processada com sucesso — **ConsultaMovSubContasV1_0** = object { response }

---
