# Prompt — Rotina de Design

> **Acione com:** `/rotina-design [semana N] [mês] [ano]`
>
> **Pré-requisito:** `/rotina-semanal` já deve ter sido executada e os arquivos
> da semana devem existir em `conteudo/[ANO]/[MES]/semana-[N]/`.

---

## O que esta rotina faz

Pega os arquivos de copy gerados pela `/rotina-semanal` e transforma em designs
prontos para editar no Canva — usando os templates oficiais da marca e o Brand Kit
`kAEN0HquLOI`. Ao final, salva os links em `designs/links-canva.md`.

---

## Templates oficiais

| Tipo de conteúdo | Template ID | Formato |
|---|---|---|
| Carrossel | `DAG-TljeV_Q` | 1080×1350px (4:5) |
| Post estático / Frase | `DAG4xGMUwKw` | 1080×1080px (1:1) ou 1080×1350px |
| Capa de protocolo / Premium | `DAHA9pzvNPY` | A4 ou personalizado |
| Documentos clínicos A4 | `DAG_nizn6NA` | A4 210×297mm |

---

## Antes de começar

1. Leia `CLAUDE.md` para confirmar Brand Kit e identidade visual
2. Identifique semana, mês e ano (a partir do comando ou pergunte ao usuário)
3. Leia os 4 arquivos da semana:
   - `conteudo/[ANO]/[MES]/semana-[N]/posts-estaticos.md`
   - `conteudo/[ANO]/[MES]/semana-[N]/carrossel.md`
   - `conteudo/[ANO]/[MES]/semana-[N]/scripts-stories-reels.md`
   - `conteudo/[ANO]/[MES]/semana-[N]/posts-simples-canva.md`
4. Crie a pasta `conteudo/[ANO]/[MES]/semana-[N]/designs/` se não existir

---

## Fluxo de execução

### Modo A — Canva MCP (preferencial quando conectado)

Execute nesta sequência para cada design da semana:

#### Para CARROSSEIS (arquivo: carrossel.md)

Para cada carrossel identificado nos arquivos:

**Passo 1 — Gerar o design via Canva**

Use a ferramenta `generate-design-structured` com:
- `design_type`: `presentation`
- `topic`: [título do carrossel]
- `audience`: "professional"
- `style`: "elegant"
- `length`: "short"
- `brand_kit_id`: `kAEN0HquLOI`
- `presentation_outlines`: um item por slide, com `title` e `description` extraídos do JSON
  do `carrossel.md`

**Mapeamento de slides JSON → outlines:**

```
slide tipo "capa"     → title: label | description: titulo
slide tipo "conteudo" → title: "numero — titulo" | description: texto
slide tipo "destaque" → title: "Destaque" | description: barra + " — " + texto
slide tipo "cta"      → title: tag | description: titulo + " — " + instrucao + " — " + cta
```

**Passo 2 — Confirmar design gerado**

Após geração, use `create-design-from-candidate` com o `job_id` e `candidate_id`
para criar o design real na conta Canva.

**Passo 3 — Registrar link**

Salve o link do design gerado no arquivo de links da semana.

---

#### Para POSTS ESTÁTICOS e POSTS SIMPLES CANVA

Use `generate-design` com:
- `design_type`: `instagram_post`
- `brand_kit_id`: `kAEN0HquLOI`
- `query`: "[frase principal do post] — post editorial estilo minimalista creme e dourado,
  tipografia Georgia, sem imagem, foco em texto"

Um design por post. Selecione o candidato mais alinhado à identidade visual.

---

### Modo B — Python PDF (offline, sem Canva MCP)

Use quando o Canva MCP não estiver disponível ou para gerar uma prévia rápida.

**Passo 1 — Extrair os JSONs de slides**

Para cada carrossel em `carrossel.md`, extraia o bloco JSON de slides e salve como
`semana-[N]-carrossel-[1|2].json`.

Exemplo de formato esperado pelo script:
```json
[
  {
    "tipo": "capa",
    "label": "Série Hormônio",
    "titulo": "Por que você acorda <em>cansada</em> todo dia"
  },
  {
    "tipo": "conteudo",
    "numero": "01",
    "titulo": "Cortisol invertido",
    "texto": "Seu cortisol deveria estar no pico às 8h. Em <strong>SOP</strong>, está no piso."
  },
  {
    "tipo": "cta",
    "tag": "Próximo passo",
    "titulo": "Quer entender o seu?",
    "instrucao": "Me manda REINO no DM e eu te explico como analisamos isso",
    "cta": "→ REINO no DM"
  }
]
```

**Passo 2 — Rodar o script**

```bash
cd [pasta do repositório]
python3 scripts/gerar-slides.py conteudo/[ANO]/[MES]/semana-[N]/carrossel-1.json \
  conteudo/[ANO]/[MES]/semana-[N]/designs/carrossel-1.pdf
```

O PDF gerado tem 2160×2700px por slide (proporção 4:5), com paleta da marca e
tipografia Georgia. Abra no Preview/Acrobat, exporte cada página como PNG
e suba direto no Instagram.

**Passo 3 — Para posts simples**

Extraia os JSONs de `posts-simples-canva.md` e execute:
```bash
python3 scripts/gerar-slides.py posts-simples.json designs/posts-simples.pdf
```

---

## Regras de qualidade para design

Antes de salvar os links ou apresentar os PDFs, verifique:

- [ ] Identidade visual está correta: creme `#F4EFE4`, marrom `#2B1A10`, ouro `#C9A435`
- [ ] Tipografia é Georgia (serif) para títulos principais
- [ ] Sem emojis no texto dos slides
- [ ] Sem travessões nos slides (use vírgula ou ponto)
- [ ] `<em>` aplicado para texto dourado (máx. 1–2 palavras por slide)
- [ ] `<strong>` aplicado para negrito estratégico (nunca decorativo)
- [ ] Nome e handle da Juliana aparecem no rodapé de todos os slides
- [ ] CRN aparece no header ou footer do slide de capa

---

## Instruções de salvamento

Salve o arquivo de links da semana em:
`conteudo/[ANO]/[MES]/semana-[N]/designs/links-canva.md`

Formato do arquivo:
```markdown
# Links de Design — Semana [N] — [Mês] [Ano]

## Carrossel 1 — [título]
Link Canva: [URL]
PDF gerado: designs/carrossel-1.pdf

## Carrossel 2 — [título] (se houver)
Link Canva: [URL]
PDF gerado: designs/carrossel-2.pdf

## Posts Estáticos
- Post 1 — [título]: [URL Canva]
- Post 2 — [título]: [URL Canva]
...

## Posts Simples Canva
PDF gerado: designs/posts-simples.pdf

## Próximos passos
→ Abra os PDFs, exporte cada página como PNG (300dpi)
→ Posts prontos para upload no Meta Business Suite
→ Agende seguindo agenda_publicacao.md
```

Confirme no chat com: `Design semana [N] pronto. Links salvos em designs/links-canva.md`

---

## Exemplos de acionamento

```
/rotina-design                      → semana atual
/rotina-design semana 2 maio        → semana 2 de maio 2026
/rotina-design semana 3 junho 2026  → explícito
```
