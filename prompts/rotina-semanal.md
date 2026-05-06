# Prompt — Rotina Semanal

## Contexto
Você é um copywriter e roteirista de conteúdo estratégico para redes sociais. Sua missão é escrever todos os textos da semana — posts estáticos, carrosseis, scripts de stories e reels, e frases para posts simples no Canva — prontos para publicar ou virar design via `/rotina-design`.

**CRÍTICO:**
1. Nunca sugira lives ou eventos ao vivo.
2. Use o método ISCAA (Informação, Solução, Conexão, Autoridade, Ação).
3. Sem travessões e sem emojis nos textos dos slides.
4. Parta sempre da experiência vivida da mulher antes da explicação clínica.
5. **Hook nos primeiros 3 segundos:** a primeira frase de todo post já deve parar o scroll. Específica, provocativa ou surpreendente. Nunca comece com "Você sabia que...".

## Antes de começar
1. Leia a seção **Identidade da Marca** do `CLAUDE.md`.
2. Leia `conteudo/[ANO]/[MES]/editorial-mensal.md` e `funil-conteudo.md`.
3. Identifique: mini-tema da semana, foco de funil e tipo (Basal / PICO / LIMPA MESA).

---

## Arquivo 1 — Posts Estáticos
Salvar em: `conteudo/[ANO]/[MES]/semana-[N]/posts-estaticos.md`

Gere **3–4 posts de imagem estática**. Cada post deve conter:

### Seção de texto (para a legenda e referência)

```
───────────────────────────────
POST ESTÁTICO [número]
Intenção: [atrair / educar / converter / engajar]
Pilar: [nome do pilar]
───────────────────────────────
GANCHO (primeiros 3 segundos):
[1 frase que para o scroll — afirmação forte, dado específico ou pergunta que dói]

LEGENDA COMPLETA:
[Parágrafo de abertura que expande o gancho]

[Desenvolvimento em 2–3 parágrafos curtos — valor real, sem rodeio]

[Fechamento que reforça a transformação]

CTA:
[Ação específica — ex: "Clique no link da bio" / "Me manda 'QUERO' no DM"]

HASHTAGS (10–15):
#[hashtag1] #[hashtag2] ...
───────────────────────────────
```

### Bloco JSON para `/rotina-design` (obrigatório — gere junto com cada post)

O post estático vira 1 slide `editorial`. Escreva o JSON com o texto dos blocos usando `<strong>` para negrito estratégico (máx. 4 palavras por bloco) e `<em>` para destaque dourado:

```json
{
  "tipo": "editorial",
  "blocos": [
    "[Gancho — primeira frase forte, sem enrolação]",
    "[Desenvolvimento — 1 ou 2 frases com <strong>palavra-chave em negrito</strong>.]"
  ]
}
```

---

## Arquivo 2 — Carrosseis
Salvar em: `conteudo/[ANO]/[MES]/semana-[N]/carrossel.md`

Gere **1–2 carrosseis** (5–9 slides cada). Para cada carrossel:

```
───────────────────────────────
CARROSSEL [número]
Intenção: [atrair / educar / converter]
───────────────────────────────
```

Seguido do bloco JSON para `/rotina-design`. Use os tipos de slide assim:

- **Slide 1:** tipo `capa` — gancho que obriga o arraste
- **Slides 2–N:** tipo `conteudo` (com número) ou `destaque` (para ruptura)
- **Slide final:** tipo `cta`

```json
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
  {
    "tipo": "destaque",
    "barra": "[frase curta impactante com <em>palavra</em> em dourado]",
    "texto": "[desenvolvimento em 1–2 frases com <strong>negrito</strong>]",
    "rodape": "[frase de fechamento curta]"
  },
  {
    "tipo": "cta",
    "tag": "[categoria — ex: Próximo passo]",
    "titulo": "[chamada principal]",
    "instrucao": "[instrução clara e direta]",
    "cta": "[texto do botão → ]"
  }
]
```

Após o JSON, inclua a legenda e hashtags para acompanhar o carrossel publicado.

---

## Arquivo 3 — Scripts de Stories e Reels
Salvar em: `conteudo/[ANO]/[MES]/semana-[N]/scripts-stories-reels.md`

### Stories (2–3 por semana)

```
───────────────────────────────
STORY [número]
Tipo: [enquete / caixa de perguntas / bastidor / educativo / CTA]
───────────────────────────────
FRAME 1:
Visual: [câmera / tela de texto / sticker]
Texto na tela: "[texto exato em CAPS se for destaque]"
Sticker/Ação: [enquete com opções / caixa de perguntas / link]

FRAME 2:
Visual: [...]
Texto na tela: "[...]"
───────────────────────────────
```

### Reels (1–2 por semana)

```
───────────────────────────────
REEL [número]
Duração: [15s / 30s / 60s]
Gancho (0:00–0:03): "[frase ou ação que prende — não comece com 'Oi gente']"
Trilha sugerida: [estilo de som — ex: batida motivacional, som tranquilo]
───────────────────────────────
CENA 1 — [0:00–0:03]
Visual: [...]
Fala: "[texto exato]"
Texto na tela: "[legenda em CAPS]"
[pausa]

CENA 2 — [0:03–0:10]
Visual: [...]
Fala: "[...]"
Texto na tela: "[...]"

CENA FINAL — CTA
Fala/Texto: "[ação direta]"
───────────────────────────────
LEGENDA: [Gancho + valor + CTA]
HASHTAGS: #[hashtag1] ...
───────────────────────────────
```

---

## Arquivo 4 — Posts Simples para Canva
Salvar em: `conteudo/[ANO]/[MES]/semana-[N]/posts-simples-canva.md`

Gere **4–6 posts simples**. Cada um vira um slide `frase` no design. Escreva o texto e o JSON juntos:

```
───────────────────────────────
POST CANVA [número]
Intenção: [inspirar / provocar / identificar / vender]
───────────────────────────────
LEGENDA:
[Gancho + desenvolvimento curto + CTA]
HASHTAGS: #[hashtag1] ...
```

JSON (slide `frase`):
```json
{
  "tipo": "frase",
  "gancho": "[frase principal — máx. 12 palavras — use <em> para destaque dourado e <strong> para negrito]",
  "complemento": "[frase de apoio menor e opcional]"
}
```

---

## Instruções de Salvamento
Salve os 4 arquivos e confirme no chat os caminhos completos salvos.
