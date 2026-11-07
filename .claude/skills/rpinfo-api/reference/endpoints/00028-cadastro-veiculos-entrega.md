# Tag 00028 — Cadastro Veiculos Entrega

2 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| GET | `/v1.0/veiculosentrega/{lastID}` | Listar Veiculos de Entrega |  |
| GET | `/v1.1/veiculosentrega/{lastID}` | Listar Veiculos de Entrega |  |

## Detalhes

### GET `/v1.0/veiculosentrega/{lastID}`

**Resumo:** Listar Veiculos de Entrega

Retorna lista de veiculos de entrega

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Na consulta deve-se informar sempre o último ID que foi lido, quando for o inicio da consulta informa-se 0. (mesmo passando 0 os dados retornam paginados) |

**Respostas:**

- `200` Lista retornada — **ListarVeiculosEntregaResponse** = object { response }

---

### GET `/v1.1/veiculosentrega/{lastID}`

**Resumo:** Listar Veiculos de Entrega

Retorna lista de veiculos de entrega

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | number | Na consulta deve-se informar sempre o último ID que foi lido, quando for o inicio da consulta informa-se 0. (mesmo passando 0 os dados retornam paginados) |

**Respostas:**

- `200` Lista retornada — **ListarVeiculosEntregaResponseV1.1** = object { response }

---
