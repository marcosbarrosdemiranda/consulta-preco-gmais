# Tag 00026 — Cadastro de Departamentos

1 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| GET | `/v1.1/departamentos` | Obter lista de departamentos cadastrados |  |

## Detalhes

### GET `/v1.1/departamentos`

**Resumo:** Obter lista de departamentos cadastrados

Consulta dados referentes aos departamentos.

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `apenasDoUsuario` | query | não | boolean | Quando verdadeiro, devolve somente os departamentos liberados para o usuário logado. Usuário sem restrição recebe a lista completa. O padrão é falso. |

**Respostas:**

- `200` Dados carregados com sucesso — **RespostaDepartamentos** = object { response }

---
