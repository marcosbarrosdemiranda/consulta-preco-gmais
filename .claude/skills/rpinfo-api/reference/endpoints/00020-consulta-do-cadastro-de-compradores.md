# Tag 00020 — Consulta do Cadastro de Compradores

2 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| GET | `/v1.3/compradores/listar/{lastID}` | Obter lista de compradores cadastrados |  |
| GET | `/v1.3/compradores/{codigo}` | Buscar comprador por código |  |

## Detalhes

### GET `/v1.3/compradores/listar/{lastID}`

**Resumo:** Obter lista de compradores cadastrados

Consulta dados referentes aos compradores.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `lastID` | path | sim | string | Código do último comprador consultado. Envie "0" caso queira consultar todos os compradores (mesmo passando 0 os dados retornam paginados) |

**Respostas:**

- `200` Dados carregados com sucesso — **ListaCompradores_V_1_2** = object { response }

---

### GET `/v1.3/compradores/{codigo}`

**Resumo:** Buscar comprador por código

Consulta dados referentes aos compradores.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | string | Código do comprador a ser consultado. |

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaComprador_V_1_2** = object { response }

---
