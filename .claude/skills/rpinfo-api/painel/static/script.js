function configurarTeste({ btnId, resultadoId, url, montarBody, montarHtmlOk, labelOcioso, labelTestando }) {
  const btn = document.getElementById(btnId);
  const resultado = document.getElementById(resultadoId);
  if (!btn || !resultado) return; // aba pode estar desabilitada (ex.: banco sem RPINFO_DB_BANCOS)

  btn.addEventListener("click", async () => {
    btn.disabled = true;
    btn.textContent = labelTestando;
    resultado.className = "resultado oculto";

    try {
      const resp = await fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(montarBody ? montarBody() : {}),
      });
      const dados = await resp.json();

      if (dados.ok) {
        resultado.className = "resultado ok";
        resultado.innerHTML = `<span class="titulo">✅ Conectado</span>${montarHtmlOk(dados)}`;
      } else {
        resultado.className = "resultado erro";
        resultado.innerHTML = `<span class="titulo">❌ Falhou</span>${dados.erro}`;
      }
    } catch (err) {
      resultado.className = "resultado erro";
      resultado.innerHTML = `<span class="titulo">❌ Erro</span>${err}`;
    } finally {
      btn.disabled = false;
      btn.textContent = labelOcioso;
      resultado.classList.remove("oculto");
      carregarHistorico(); // mantém a aba Histórico sempre em dia, mesmo se não estiver aberta
    }
  });
}

configurarTeste({
  btnId: "btn-testar-api",
  resultadoId: "resultado-api",
  url: "/api/testar-api",
  labelOcioso: "Testar API",
  labelTestando: "Testando...",
  montarHtmlOk: (d) => `
    Host: <code>${d.host}</code><br>
    Usuário: <code>${d.usuario}</code><br>
    Token: <code>${d.token_mascarado}</code><br>
    Expira em: <code>${d.expira_em}</code>${d.expira_em_min != null ? ` (~${d.expira_em_min} min)` : ""}
  `,
});

configurarTeste({
  btnId: "btn-testar-banco",
  resultadoId: "resultado-banco",
  url: "/api/testar-banco",
  labelOcioso: "Testar banco",
  labelTestando: "Testando...",
  montarBody: () => ({ banco: document.getElementById("banco").value }),
  montarHtmlOk: (d) => `
    Banco: <code>${d.banco}</code><br>
    Host: <code>${d.host}:${d.porta}</code><br>
    Usuário: <code>${d.usuario}</code><br>
    Versão: <code>${d.versao_postgres}</code>
  `,
});

configurarTeste({
  btnId: "btn-testar-negocio",
  resultadoId: "resultado-negocio",
  url: "/api/testar-endpoint-negocio",
  labelOcioso: "Testar endpoint",
  labelTestando: "Testando...",
  montarHtmlOk: (d) => `
    Endpoint: <code>${d.endpoint}</code><br>
    Host: <code>${d.host}</code><br>
    Itens retornados: <code>${d.quantidade}</code><br>
    Amostra: <code>${JSON.stringify(d.amostra)}</code>
  `,
});

// --- Ofertas por loja ---
async function carregarLojas() {
  const select = document.getElementById("loja-ofertas");
  if (!select) return;
  select.innerHTML = `<option value="">Carregando lojas...</option>`;
  try {
    const resp = await fetch("/api/unidades");
    const dados = await resp.json();
    if (!dados.ok || !dados.lojas.length) {
      select.innerHTML = `<option value="">Nenhuma loja encontrada (${dados.erro || "lista vazia"})</option>`;
      return;
    }
    select.innerHTML = dados.lojas
      .map((l) => `<option value="${l.codigo}" data-cnpj="${l.cnpj}">${l.codigo} — ${l.nome}</option>`)
      .join("");
  } catch (err) {
    select.innerHTML = `<option value="">Erro ao carregar lojas: ${err}</option>`;
  }
}

// Guarda a última busca pra poder re-renderizar (agrupado ou não) sem rebuscar na API.
let ultimasOfertas = [];

// Agrupa linhas que só variam por sabor/fragrância (mesmo nome + marca + preço, código de
// barras diferente) — puramente visual no navegador, não altera o que veio da API.
function agruparOfertas(ofertas) {
  const grupos = new Map();
  for (const o of ofertas) {
    const chave = `${(o.nomeProduto || "").trim().toLowerCase()}|${(o.marca || "").trim().toLowerCase()}|${o.precoAtual}`;
    if (!grupos.has(chave)) {
      grupos.set(chave, { ...o, _variacoes: 1, _barras: o.codigoBarras ? [o.codigoBarras] : [] });
    } else {
      const g = grupos.get(chave);
      g._variacoes += 1;
      if (o.codigoBarras) g._barras.push(o.codigoBarras);
    }
  }
  return [...grupos.values()];
}

function renderTabelaOfertas() {
  const wrap = document.getElementById("tabela-ofertas-wrap");
  const agrupar = document.getElementById("agrupar-ofertas")?.checked;
  const linhas = agrupar ? agruparOfertas(ultimasOfertas) : ultimasOfertas;

  if (!linhas.length) {
    wrap.innerHTML = "";
    return;
  }

  wrap.innerHTML = `
    ${agrupar ? `<p class="aviso-agrupado">${linhas.length} produto(s) único(s) (de ${ultimasOfertas.length} ofertas, agrupando sabores/fragrâncias repetidos)</p>` : ""}
    <table class="tabela-historico">
      <thead><tr><th>Código</th><th>Produto</th><th>Marca</th><th>Preço antes</th><th>Preço oferta</th><th>Cód. barras</th></tr></thead>
      <tbody>${linhas.map((o) => `
        <tr>
          <td>${o.codigoProduto}</td>
          <td>${o.nomeProduto}</td>
          <td>${o.marca || ""}</td>
          <td>R$ ${Number(o.precoAnterior).toFixed(2)}</td>
          <td>R$ ${Number(o.precoAtual).toFixed(2)}</td>
          <td>${o._variacoes > 1
            ? `<span title="${o._barras.join(", ")}">${o._variacoes} variações</span>`
            : (o.codigoBarras || "")}</td>
        </tr>`).join("")}</tbody>
    </table>`;
}

document.getElementById("agrupar-ofertas")?.addEventListener("change", renderTabelaOfertas);

document.getElementById("btn-testar-ofertas")?.addEventListener("click", async () => {
  const btn = document.getElementById("btn-testar-ofertas");
  const resultado = document.getElementById("resultado-ofertas");
  const wrap = document.getElementById("tabela-ofertas-wrap");
  const select = document.getElementById("loja-ofertas");
  const opcao = select.selectedOptions[0];

  if (!opcao || !opcao.value) {
    resultado.className = "resultado erro";
    resultado.innerHTML = `<span class="titulo">❌ Erro</span>Escolha uma loja primeiro.`;
    resultado.classList.remove("oculto");
    return;
  }

  btn.disabled = true;
  btn.textContent = "Buscando...";
  resultado.className = "resultado oculto";
  wrap.innerHTML = "";

  try {
    const resp = await fetch("/api/ofertas", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        codigo: opcao.value,
        cnpj: opcao.dataset.cnpj,
        departamento: document.getElementById("departamento-ofertas").value || undefined,
        setor: document.getElementById("setor-ofertas").value || undefined,
      }),
    });
    const dados = await resp.json();

    if (dados.ok) {
      resultado.className = "resultado ok";
      resultado.innerHTML = `<span class="titulo">✅ ${dados.quantidade} oferta(s)</span>Endpoint: <code>${dados.endpoint}</code>`;
      ultimasOfertas = dados.ofertas;
      renderTabelaOfertas();
    } else {
      resultado.className = "resultado erro";
      resultado.innerHTML = `<span class="titulo">❌ Falhou</span>${dados.erro}`;
    }
  } catch (err) {
    resultado.className = "resultado erro";
    resultado.innerHTML = `<span class="titulo">❌ Erro</span>${err}`;
  } finally {
    btn.disabled = false;
    btn.textContent = "Buscar ofertas";
    resultado.classList.remove("oculto");
    carregarHistorico();
  }
});

// --- Abas ---
document.querySelectorAll(".aba-botao").forEach((botao) => {
  botao.addEventListener("click", () => {
    document.querySelectorAll(".aba-botao").forEach((b) => b.classList.remove("ativa"));
    document.querySelectorAll(".aba").forEach((a) => a.classList.remove("ativa"));
    botao.classList.add("ativa");
    document.getElementById(`aba-${botao.dataset.aba}`).classList.add("ativa");
    if (botao.dataset.aba === "historico") carregarHistorico();
    if (botao.dataset.aba === "ofertas") carregarLojas();
  });
});

// --- Histórico ---
async function carregarHistorico() {
  const tbody = document.querySelector("#tabela-historico tbody");
  if (!tbody) return;

  const resp = await fetch("/api/historico");
  const registros = await resp.json();

  tbody.innerHTML = registros.length
    ? registros.map((r) => `
        <tr>
          <td>${new Date(r.criado_em).toLocaleString("pt-BR")}</td>
          <td>${r.categoria}</td>
          <td>${r.subtipo}</td>
          <td>${r.ok ? "✅" : "❌"}</td>
          <td><button class="botao-secundario botao-achado" data-id="${r.id}">Gerar achado</button></td>
        </tr>
      `).join("")
    : `<tr><td colspan="5">Nenhum teste rodado ainda.</td></tr>`;

  document.querySelectorAll(".botao-achado").forEach((b) => {
    b.addEventListener("click", () => gerarAchado(b.dataset.id));
  });
}

async function gerarAchado(id) {
  const resp = await fetch(`/api/gerar-achado/${id}`, { method: "POST" });
  const dados = await resp.json();
  const caixa = document.getElementById("achado-caixa");
  const texto = document.getElementById("achado-texto");
  texto.value = dados.ok ? dados.texto : `Erro: ${dados.erro}`;
  caixa.classList.remove("oculto");
}

document.getElementById("btn-atualizar-historico")?.addEventListener("click", carregarHistorico);
document.getElementById("btn-copiar-achado")?.addEventListener("click", () => {
  const texto = document.getElementById("achado-texto");
  texto.select();
  navigator.clipboard?.writeText(texto.value);
});
