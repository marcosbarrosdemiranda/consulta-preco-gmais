# Tag 00027 — Fiscal

1 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| GET | `/v1.2/fiscal/getnfecupom` | Nota fiscal eletrônica emitida para um determinado cupom fiscal |  |

## Detalhes

### GET `/v1.2/fiscal/getnfecupom`

**Resumo:** Nota fiscal eletrônica emitida para um determinado cupom fiscal

Buscar nota fiscal eletrônica emitida para um determinado cupom fiscal.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `unidade` | query | sim | string | Unidade do cupom fiscal |
| `cupom` | query | sim | string | Número do cupom fiscal |
| `pdv` | query | sim | string | Código do PDV onde o cupom foi emitido |

**Respostas:**

- `200` Dados carregados com sucesso — **NfeByCupomV1_2** = object { response }

---
