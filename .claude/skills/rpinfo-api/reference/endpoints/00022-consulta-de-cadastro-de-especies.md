# Tag 00022 — Consulta de Cadastro de Espécies

1 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| GET | `/v1.0/especies` | Recuperar o cadastro de espécies |  |

## Detalhes

### GET `/v1.0/especies`

**Resumo:** Recuperar o cadastro de espécies

Recuperar o cadastro de espécies no ERP

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Respostas:**

- `200` Dados carregados com sucesso — **EspeciesResponse** = object { response }

---
