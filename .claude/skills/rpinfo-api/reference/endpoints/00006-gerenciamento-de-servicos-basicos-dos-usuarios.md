# Tag 00006 — Gerenciamento de serviços básicos dos usuários

6 endpoint(s).

## Lista rápida

| Método | Path | Resumo | Depreciado |
|---|---|---|---|
| POST | `/v1.0/mensagem` | Enviar mensagem entre usuários |  |
| PUT | `/v1.0/usuarios/{codigo}/bloquear` | Bloquear Usuário |  |
| PUT | `/v1.0/usuarios/{codigo}/desativar` | Desativar Usuário |  |
| GET | `/v1.2/usuarios/` | Obter cadastro de usuarios |  |
| GET | `/v1.2/usuarios/{codigo}` | Obter dados do usuario |  |
| GET | `/v1.2/usuarios/{codigo}/detalhado` | Obter dados do usuario detalhado |  |

## Detalhes

### POST `/v1.0/mensagem`

**Resumo:** Enviar mensagem entre usuários

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Request body** (application/json, obrigatório: True):

- **PostMensagemUsuario** = object { assunto, texto, usuariosDestino }

**Respostas:**

- `200` Mensagem enviada com sucesso — **RespostaPostMensagemUsuario** = object { status, appVersion, messages, content }

---

### PUT `/v1.0/usuarios/{codigo}/bloquear`

**Resumo:** Bloquear Usuário

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do Usuário |

**Respostas:**

- `200` Usuário Bloqueado — **BloquearUsuarioResponse** = object { status, appVersion, messages, content }

---

### PUT `/v1.0/usuarios/{codigo}/desativar`

**Resumo:** Desativar Usuário

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Código do Usuário |

**Respostas:**

- `200` Usuário Desativado — **DesativarUsuarioResponse** = object { status, appVersion, messages, content }

---

### GET `/v1.2/usuarios/`

**Resumo:** Obter cadastro de usuarios

Obter o cadastro de usuarios do sistema ERP

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |

**Respostas:**

- `200` Cadastro de usuários retornado — **ConsultarCadUsuariosResponseV1_2** = object { response }

---

### GET `/v1.2/usuarios/{codigo}`

**Resumo:** Obter dados do usuario

Obter dados do usuario do sistema ERP

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Codigo do usuario |

**Respostas:**

- `200` Dados do usuário retornado — **ConsultarDadosUsuarioResponseV1_2** = object { response }

---

### GET `/v1.2/usuarios/{codigo}/detalhado`

**Resumo:** Obter dados do usuario detalhado

Obter dados do usuario detalhado do sistema ERP

**Parâmetros:**

| Nome | Em | Obrigatório | Tipo | Descrição |
|---|---|---|---|---|
| `token` | header | sim | string | token de autenticação |
| `codigo` | path | sim | number | Codigo do usuario |

**Respostas:**

- `200` Dados do usuário retornado — **ConsultarDadosUsuarioDetalhadoResponseV1_2** = object { response }

---
