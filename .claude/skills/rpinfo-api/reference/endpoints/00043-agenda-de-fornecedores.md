# Tag 00043 — Agenda de Fornecedores

1 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| GET | `/v1.0/agendas/fornecedor/lastId/{lastId}` | Consulta as agendas dos fornecedores |  |

## Detalhes

### GET `/v1.0/agendas/fornecedor/lastId/{lastId}`

**Resumo:** Consulta as agendas dos fornecedores

Este endpoint retorna as agendas dos fornecedores, permitindo filtros opcionais por período (`dataInicio`, `dataFim`), fornecedor, comprador, unidade, horário e `lastId` para paginação.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de autenticação |
| `lastId` | path | sim | integer | Último ID retornado para paginação |
| `dataInicio` | query | não | string | Data de início no formato `dd-MM-yyyy` |
| `dataFim` | query | não | string | Data de fim no formato `dd-MM-yyyy` |
| `unidade` | query | não | string | Código da unidade |
| `comprador` | query | não | string | Código do comprador |
| `fornecedor` | query | não | string | Código do fornecedor |
| `horario` | query | não | string | Horário da agenda |
| `limit` | query | não | integer | Limite de registros a serem retornados |

**Respostas:**

- `200` Requisição processada com sucesso — **ResponseAgendaFornecedores_V_1_0** = object { response }

---
