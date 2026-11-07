# Tag 00047 — Cenarios

1 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| GET | `/v1.0/cenarios/preco/produtos` | Retorna os produtos do cenário de preço |  |

## Detalhes

### GET `/v1.0/cenarios/preco/produtos`

**Resumo:** Retorna os produtos do cenário de preço

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | Token de autenticação |
| `codigoCenario` | query | sim | integer |  |
| `produto` | query | não | string |  |
| `lastId` | query | sim | integer |  |
| `limit` | query | não | integer |  |

**Respostas:**

- `200` OK — **response_v1.0_cenarios_preco_produtos** = object { response }

---
