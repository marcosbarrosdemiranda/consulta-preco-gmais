# Tag 00045 — Transportadores

2 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| GET | `/v1.0/transportadores` | Consultar todas as transportadoras cadastradas |  |
| GET | `/v1.1/transportadores` | Consultar todas as transportadoras cadastradas |  |

## Detalhes

### GET `/v1.0/transportadores`

**Resumo:** Consultar todas as transportadoras cadastradas

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaConsultaTransportadores** = object { response }

---

### GET `/v1.1/transportadores`

**Resumo:** Consultar todas as transportadoras cadastradas

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaConsultaTransportadoresV1** = object { response }

---
