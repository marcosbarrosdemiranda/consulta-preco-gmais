# Painel de testes (ferramenta opcional)

A skill inclui, em `painel/`, um painel web local **opcional** — não é necessário pra skill
funcionar, é só um atalho visual pra quem quiser ver os resultados de teste da API (e,
opcionalmente, do Postgres direto) num navegador em vez de ler log/JSON cru.

## Por que existe

Ao integrar com uma API nova, a forma mais confiável de confirmar um achado (ex.: "esse
endpoint está depreciado", "esse campo vem num formato diferente do spec") é rodar uma chamada
real e olhar a resposta — não só ler o spec. O painel nasceu pra tornar esse ciclo (testar →
olhar o resultado → documentar o achado) rápido e visual, em vez de escrever um script
descartável toda vez. Ver `pegadinhas.md` — vários dos achados documentados ali foram
confirmados rodando um teste no painel primeiro.

## O que ele faz

- **Conexão API-Banco** — autentica na API (`POST /v1.2/auth`) e, se configurado, testa conexão
  direta ao Postgres (`SELECT version()`). Dois testes independentes, sempre somente leitura.
- **Endpoint de Negócio** — round-trip completo: autentica, pega o token, chama um endpoint real
  de leitura (`GET /v1.6/unidades`) — confirma que o token funciona ponta a ponta.
- **Ofertas por Loja** — busca as ofertas de preço vigentes de uma loja (`GET
  /v1.0/produtounidade/ofertas`), com paginação automática.
- **Histórico** — guarda (SQLite local) todos os testes já rodados e tem um botão "Gerar
  achado" que monta um rascunho de texto no formato deste próprio arquivo (`pegadinhas.md`) a
  partir de um teste real — **só rascunho**, nunca escreve sozinho no arquivo da skill; revisar
  e colar manualmente.

## Como usar

Ver `painel/README.md` pro passo a passo completo. Resumo:

```powershell
cd painel
copy .env.example .env   # preencher com os dados da SUA instalação RP Info
pip install -r requirements.txt
python app.py
```

Abre em `http://127.0.0.1:5000`, só nesta máquina.

## Por que é genérico (não hardcoded pro cliente de origem)

A skill é copiada/instalada em várias máquinas e usada por clientes diferentes da RP Info — o
painel segue a mesma regra de credenciais do resto da skill (nunca hardcoded, sempre via `.env`
próprio, nunca versionado). A única coisa que varia entre instalações além de host/usuário/senha
é a lista de bancos do Postgres (nomes de banco são específicos de cada instalação do ERP) —
por isso ela vem de `RPINFO_DB_BANCOS` no `.env`, e não de uma lista fixa no código. Se o seu
projeto já tem um mapeamento de schema (como em `reference/db-schema/`), é esse o lugar pra
confirmar os nomes certos antes de preencher essa variável.

## Replicando o padrão num projeto específico

Quem estiver usando a skill dentro de um projeto de cliente (não só a skill isolada) pode manter
uma segunda cópia do painel fora da pasta da skill, já configurada/testada contra o ambiente
daquele cliente específico (foi o que aconteceu no projeto de origem desta skill — ver
`../../../painel/` na raiz do repositório onde esta skill foi desenvolvida, se ele estiver
disponível). Isso evita misturar configuração/dado de um cliente específico com a pasta
portátil da skill, que continua genérica.
