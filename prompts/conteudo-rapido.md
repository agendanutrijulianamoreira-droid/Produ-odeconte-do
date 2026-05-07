# Prompt — Conteúdo Rápido

> **Acione com:** `/conteudo-rapido [tema] [formato]`
>
> **Para:** Criar 1 peça de conteúdo isolada em menos de 5 minutos, sem precisar
> rodar o fluxo semanal completo. Use quando surgir uma oportunidade, uma tendência
> ou um insight clínico que precisa virar post hoje.

---

## Antes de começar

1. Leia `CLAUDE.md` — Identidade da Marca e Regras Invioláveis de Escrita.
2. Leia `prompts/neuro-copy.md` — **obrigatório antes de escrever a primeira palavra.** Os 7 gatilhos neurais determinam como cada frase é construída.
3. Leia `prompts/humanizacao.md` — voz real da Juliana, exemplos antes/depois, filtro anti-IA.
4. Se existir editorial do mês em `conteudo/[ANO]/[MES]/editorial-mensal.md`, leia para
   garantir que o post nao foge da narrativa do mês.

---

## Como processar o pedido

### Identificar automaticamente:

1. **Tema** — explícito no comando ou inferido do contexto
2. **Formato** — se não especificado, sugira o mais adequado para o tema:
   - Dado clínico surpreendente → Carrossel ou Post estático
   - Bastidor da clínica / resposta a pergunta de paciente → Reel ou Stories
   - Frase de impacto / virada de perspectiva → Post simples Canva
   - Tendência ou notícia do nicho → Reel curto (15–30s)
3. **Estágio de funil** — se não especificado, default para **Topo** (maior alcance)

---

## Estrutura de entrega (um bloco por formato)

### Para POST ESTÁTICO

```
───────────────────────────────────────────────────
CONTEÚDO RÁPIDO — Post Estático
Tema: [tema]
Funil: [Topo / Meio / Fundo]
───────────────────────────────────────────────────

TEXTO DO SLIDE (máx. 10 palavras visíveis):
[frase principal — use <em> para destaque dourado e <strong> para negrito]

GANCHO (1ª linha da legenda — para o scroll):
[não começa com "Você sabia que" — começa com experiência]

LEGENDA COMPLETA:
[3–5 parágrafos curtos, max 3 linhas cada]

CTA:
[uma ação específica]

HASHTAGS (10–12):
#[hashtag1] #[hashtag2] ...

JSON PARA DESIGN:
{
  "tipo": "editorial",
  "blocos": [
    "[gancho do slide — frase principal]",
    "[frase de desenvolvimento com <strong>negrito</strong> estratégico]"
  ]
}
───────────────────────────────────────────────────
```

---

### Para CARROSSEL (entregas: copy + JSON)

```
───────────────────────────────────────────────────
CONTEÚDO RÁPIDO — Carrossel
Tema: [tema]
Funil: [Topo / Meio / Fundo]
Total de slides: [N + capa + CTA]
───────────────────────────────────────────────────

LEGENDA DO POST:
[Gancho + 2 frases de valor + CTA]
HASHTAGS: #...

JSON DOS SLIDES:
[
  {
    "tipo": "capa",
    "label": "[série ou tema em poucas palavras]",
    "titulo": "[frase que para o scroll — use <em> para destaque dourado]"
  },
  {
    "tipo": "conteudo",
    "numero": "01",
    "titulo": "[título do ponto]",
    "texto": "[explicação em 1–2 frases com <strong>negrito</strong> estratégico]"
  },
  ...
  {
    "tipo": "cta",
    "tag": "[categoria]",
    "titulo": "[chamada principal]",
    "instrucao": "[instrução clara]",
    "cta": "[texto do botão →]"
  }
]
───────────────────────────────────────────────────
```

---

### Para REEL

```
───────────────────────────────────────────────────
CONTEÚDO RÁPIDO — Reel
Tema: [tema]
Duração: [15s / 30s / 60s]
Formato: [talking head / voz off + texto na tela]
───────────────────────────────────────────────────

GANCHO (0:00–0:03):
Texto na tela: "[frase em CAPS, máx. 6 palavras]"
Fala: "[o que Juliana diz nos primeiros 3 segundos]"

CENAS:
[CENA 2 — 0:03–0:XX]
Visual: [o que aparece na tela]
Fala: "[texto exato — frases curtas, pontuação como pausa]"
Texto na tela: "[legenda em CAPS se houver]"
[pausa]

[repete o padrão para cada cena]

[CENA FINAL — CTA]
Fala/Texto: "[ação única e direta]"

TRILHA: [estilo sugerido — ex: "levemente motivacional, sem letra"]
LEGENDA: [gancho curto + 1 frase de contexto + CTA]
HASHTAGS: #...
───────────────────────────────────────────────────
```

---

### Para STORIES (sequência de 3–5)

```
───────────────────────────────────────────────────
CONTEÚDO RÁPIDO — Sequência de Stories
Tema: [tema]
Objetivo: [engajar / converter / educar / bastidor]
───────────────────────────────────────────────────

STORY 1 — [Tipo: texto / bastidor / enquete]
Texto na tela: "[texto principal em CAPS ou formato normal]"
Visual: [câmera / fundo de cor / imagem]
Sticker: [nenhum / enquete: "[opção A]" vs "[opção B]"]

STORY 2 — [Tipo]
...

STORY FINAL — CTA
Texto: "[instrução direta]"
Sticker: [link / caixinha de perguntas / enquete final]
───────────────────────────────────────────────────
```

---

### Para POST SIMPLES CANVA (frase de impacto)

```
───────────────────────────────────────────────────
CONTEÚDO RÁPIDO — Post Simples Canva
Tema: [tema]
───────────────────────────────────────────────────

FRASE PRINCIPAL (máx. 12 palavras):
[use <em> para dourado e <strong> para negrito]

COMPLEMENTO (opcional, menor — máx. 8 palavras):
[frase de apoio]

LEGENDA: [gancho + 2 frases + CTA]
HASHTAGS: #...

JSON:
{
  "tipo": "frase",
  "gancho": "[frase principal com marcações]",
  "complemento": "[frase de apoio, se houver]"
}
───────────────────────────────────────────────────
```

---

## Onde salvar (opcional)

Se o usuário não especificar, salve em:
`conteudo/[ANO]/[MES]/avulsos/[data]_[tema-em-kebab-case].md`

Exemplo: `conteudo/2026/maio/avulsos/07-05_sop-compulsao-noturna.md`

---

## Aplicar humanizacao.md antes de entregar

**Obrigatório:** Antes de apresentar qualquer copy gerado neste módulo, aplique
o filtro completo de `prompts/humanizacao.md`. Não pule o checklist.

Se algum item falhar, reescreva antes de entregar.

---

## Exemplos de acionamento

```
/conteudo-rapido compulsão noturna e cortisol → carrossel
/conteudo-rapido por que a calça não fecha na TPM → post estático
/conteudo-rapido bastidor da semana → stories 5 frames
/conteudo-rapido resultado de paciente sem revelar identidade → reel 30s
/conteudo-rapido Dia V de hoje — oferta Método Reino → post de conversão
```
