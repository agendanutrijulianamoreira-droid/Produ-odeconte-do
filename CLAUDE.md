# Sistema de Produção de Conteúdo

Este repositório é o cérebro da produção de conteúdo. O Claude executa rotinas periódicas para gerar estratégia anual, editorial mensal e posts semanais prontos para publicar ou editar no Canva.

---

## Referência Rápida de Comandos

| Comando | Frequência | O que faz |
|---|---|---|
| `/rotina-anual [ano]` | 1× por ano | Gera linha editorial anual |
| `/rotina-mensal [mês] [ano]` | 1× por mês | Gera editorial + funil do mês |
| `/rotina-semanal [semana N] [mês]` | Toda segunda-feira | Gera os 4 arquivos da semana |
| `/rotina-design [semana N] [mês]` | Após a semanal | Cria designs no Canva ou PDF |
| `/conteudo-rapido [tema] [formato]` | Qualquer momento | 1 post urgente em < 5 min |

---

## REGRAS INVIOLÁVEIS DE ESCRITA

```
PROIBIDO em absolutamente qualquer peça de conteúdo:
- Travessão ( — ) em qualquer posição. Use virgula ou ponto.
- Emoji no texto de slides e roteiros. Só na legenda publicada, com parcimonia.
- "Você sabia que", "Descubra", "Conheça", "Aprenda" abrindo qualquer frase.
- Adjetivos genéricos: "incrível", "poderoso", "transformador", "revolucionário".
- Superlativo vazio: "a melhor", "único no Brasil", "método exclusivo".
- Frases que qualquer outra nutricionista poderia ter escrito.
- CTA duplo ou triplo em um mesmo post.
```

## REGRA INVIOLÁVEL — Humanização + Neuro-Copy

**Toda geração de conteúdo lê obrigatoriamente, nesta ordem:**
1. `prompts/neuro-copy.md` — gatilhos neurais e estrutura de frase
2. `prompts/humanizacao.md` — voz real da Juliana e exemplos antes/depois

Sem exceção. Sem "post rápido" que saia sem esses dois filtros.

---

## Geração de Slides (PDF + PNG)

O script `scripts/gerar-slides.py` gera os slides em PDF e converte para PNG automaticamente:

```bash
# PDF apenas
python3 scripts/gerar-slides.py slides.json saida.pdf

# PDF + PNGs 2160×2700px prontos para Instagram
python3 scripts/gerar-slides.py slides.json saida.pdf --png
```

Os PNGs ficam na pasta `saida_slides/slide_01.png`, `slide_02.png`, etc.
Cada PNG sai em 2160×2700px (proporção 4:5 — padrão Instagram).

---

## Tabela de Produtos e Preços (atualizada)

| Produto | Preço | Status |
|---|---|---|
| Consulta avulsa | R$300 | Ativo — porta de entrada para o Trimestral |
| Método REINO Trimestral | R$790 | Produto âncora principal |
| Comunidade / Grupos | R$97/mês | Em lançamento |
| Protocolo PDF Sazonal | R$67 | Em lançamento (início: pré/pós canetas) |
| Teste Genético + 1 consulta | R$1.200 | Criado — sem CTA ativo |
| Teste Genético + 3 consultas | R$1.650 | Criado — sem CTA ativo |
| E-book | R$27–47 | Em desenvolvimento |

**Regra de CTA por objetivo da semana — nunca misturar:**
- Semana de autoridade → CTA: seguir + salvar
- Semana de conversão → CTA: "Comente [PALAVRA]" ou WhatsApp para o Trimestral
- Semana de lançamento → CTA: link da página de vendas do produto em foco

---

## Sistema de Memória — Histórico de Semanas

Após cada semana entregue, o Claude registra em `historico_semanas.md`:

```markdown
## Semana [N] — [DATA]
- Tema: [tema]
- Objetivo: [Autoridade / Conversão / Lançamento]
- Gancho slide 1: [texto exato usado]
- Receita: [nome da receita]
- CTA: [ação usada]
- Produto em foco: [produto + preço]
- Ajuste pedido: [se a Juliana pediu alguma mudança]
```

Leia `historico_semanas.md` antes de cada semana nova para não repetir gancho, receita ou CTA idêntico.

---

```
HANDLE INSTAGRAM: @nutridamulhermoderna
BRAND KIT CANVA:  kAEN0HquLOI

TEMPLATES OFICIAIS:
  Carrossel:      DAG-TljeV_Q
  Post entrega:   DAG4xGMUwKw
  Capa premium:   DAHA9pzvNPY
  Docs A4:        DAG_nizn6NA

PALETA:
  Creme:          #F4EFE4
  Marrom escuro:  #2B1A10
  Ouro:           #C9A435

TIPOGRAFIA:       Georgia (serif)
FORMATO POSTS:    2160x2700px (4:5) — proporção padrão Instagram
```

---

## Identidade da Marca

> Preencha esta seção antes de rodar qualquer rotina.

```
NOME:           Juliana Moreira — Nutricionista

NICHO:          Nutrição para mulheres com desregulação hormonal (SOP, endometriose,
                candidíase e miomas), com foco em emagrecimento sem efeito sanfona,
                redução de inchaço e melhora de energia.

PÚBLICO-ALVO:   Mulheres de 30 a 45 anos. Empreendedoras ou com rotina intensa.
                Nao é a mulher que quer "emagrecer uns quilinhos".
                É a que JÁ TENTOU DE TUDO e continua sem resultado:

                Trilha da frustração (ela passou por tudo isso, nessa ordem):
                1. Fez dieta restritiva. Funcionou 3 semanas. Voltou tudo.
                2. Foi ao endocrinologista. Exames "dentro do normal". Saiu sem resposta.
                3. Tomou remédio para tireoide, metformina, ou anticoncepcional.
                   Resultado mínimo ou efeito colateral insuportável.
                4. Fez exercício regularmente por meses. A balança nao moveu.
                5. Tentou jejum intermitente, low carb, detox, chá de X ervas.
                6. Cogitou bariátrica. Algumas já consultaram.
                7. Algumas já usaram caneta (GLP-1/Ozempic/Wegovy): perderam
                   peso mas emagraram massa muscular, ficaram fracas, ou
                   engordaram tudo de volta quando pararam.

                O que ela sente agora:
                - Culpa: acha que o problema é falta de disciplina ou força de vontade
                - Resignação: "meu metabolismo é lento", "é genética", "nao serve pra mim"
                - Desconfiança: já comprou promessa demais, nao acredita mais fácil
                - Medo: de fazer mais uma coisa e falhar de novo
                - Raiva: do próprio corpo, da medicina que nao deu resposta
                - Esperança reprimida: ainda acredita que existe uma saída

                O que ela REALMENTE quer (mais fundo que "emagrecer"):
                - Entender POR QUE o corpo dela nao responde como o de outras
                - Liberdade com comida, sem culpa, sem restricao extrema
                - Energia de volta para a rotina
                - Sentir-se bem no próprio corpo — nao num corpo perfeito, no seu
                - Alguém que finalmente LEIA o caso dela, nao protocolo genérico
                - Sair do ciclo de tentativa, resultado, recaída, culpa

                Frases que ela fala para si mesma (o copy deve espelhar isso):
                "Eu como bem, faco exercício e o peso nao sai."
                "O médico disse que está tudo normal. Mas eu sei que nao está."
                "Já tentei de tudo. Nao funciona pra mim."
                "Será que o problema sou eu?"
                "Pensei em fazer bariátrica. Mas tenho medo."
                "Fiz a caneta, perdi peso, parei, engordei tudo de volta mais fraca."
                "Meu corpo sabota tudo que eu faço."
                "Tenho medo de começar mais uma coisa e nao conseguir."

                A virada de identidade que converte essa mulher:
                "Nao é você. É que ninguém leu o seu corpo direito até agora."

DORES:          - Tentou tudo e nada funcionou de forma duradoura
                - O médico disse que está "dentro do normal" — mas ela sabe que nao está
                - Perdeu músculo e ficou fraca com a caneta, ou engordou tudo de volta
                - Cogita bariátrica e tem medo de se arrepender
                - Sente que o problema é ela, nao a estratégia
                - Exausta de começar e parar ciclos de dieta
                - Inchaço que nao passa, cansaço que nao vai embora, ciclo bagunçado
                - Compulsao noturna que aparece mesmo quando o dia foi "perfeito"

DESEJOS:        - Entender POR QUE o corpo dela nao responde — nao mais uma dieta
                - Liberdade com comida sem culpa, sem cortar tudo
                - Energia de volta para funcionar bem na rotina intensa
                - Sentir-se bem no seu próprio corpo — reconhecer-se no espelho
                - Um protocolo feito para o caso específico dela, nao genérico
                - Sair de vez do ciclo: tenta, perde, recai, engorda, culpa

TRANSFORMACAO:  De exausta, inchada, sem resposta e quase desistindo
                → Leve, regulada, entendendo o próprio corpo e com protocolo que funciona

PRODUTOS (escada de valor):
  Entrada:      E-book (R$47) | Protocolos sazonais (R$47–97)
  Recorrência:  Comunidade (R$47–97/mês) — em breve
  Conversão:    Consulta (R$200)
  Core:         Método Reino Trimestral (R$600)
  Upsell:       Teste genético com devolutiva (R$1.000–R$1.200) | Acompanhamento avançado 3–6 meses (R$3.000–R$5.000+)

OBJETIVO:       Manter recorrência de faturamento de R$16.000/mês (foco em previsibilidade).
                Construção de autoridade (abril–junho 2026) para aumento de preços em julho.

TOM DE VOZ:     Direto, estratégico e acolhedor. Sem romantização. Foco em solução
                prática. Autoridade sem arrogância. Conversa de especialista que
                entende a rotina real da mulher que trabalha muito e não tem tempo a perder.

DIFERENCIAIS:   - Nutrição baseada em exames bioquímicos e genéticos
                - Acompanhamento próximo e estratégico
                - Método estruturado com ajustes semanais (Método Reino Trimestral)
                - Foco em resultados reais, não dieta restritiva

OBJEÇÕES COMUNS:"Já tentei de tudo e não funciona"
                "Não tenho tempo"
                "É caro"
                "Não sei se vou conseguir seguir"
                "Tenho medo de começar e parar de novo"
```

---

## Estrutura de Pastas

```
estrategia/
  [ano]/
    linha-editorial-anual.md     ← gerado por /rotina-anual

conteudo/
  [ano]/
    [mes]/
      editorial-mensal.md        ← gerado por /rotina-mensal
      funil-conteudo.md          ← gerado por /rotina-mensal
      semana-1/
        posts-estaticos.md       ← gerado por /rotina-semanal
        carrossel.md             ← gerado por /rotina-semanal
        scripts-stories-reels.md ← gerado por /rotina-semanal
        posts-simples-canva.md   ← gerado por /rotina-semanal
        designs/
          links-canva.md         ← gerado por /rotina-design (links diretos no Canva)
      semana-2/
        ...
      semana-3/
        ...
      semana-4/
        ...

prompts/
  rotina-anual.md
  rotina-mensal.md
  rotina-semanal.md
```

---

## Como executar — Fluxo completo

Execute os comandos nesta ordem. Cada um depende do anterior.

### 1. `/rotina-anual` — Uma vez por ano
Execute em dezembro para o ano seguinte (ou quando precisar).

```
/rotina-anual        → gera para o ano atual
/rotina-anual 2027   → gera para 2027
```

Gera: `estrategia/[ANO]/linha-editorial-anual.md`

---

### 2. `/rotina-mensal` — Todo início de mês
Execute na primeira semana de cada mês.

```
/rotina-mensal             → gera o mês atual
/rotina-mensal junho       → gera junho
/rotina-mensal junho 2026  → explícito
```

Gera:
- `conteudo/[ANO]/[MES]/editorial-mensal.md`
- `conteudo/[ANO]/[MES]/funil-conteudo.md`

---

### 3. `/rotina-semanal` — Toda semana (segunda-feira)
Execute toda segunda-feira ou domingo à noite.

```
/rotina-semanal                    → gera a semana atual
/rotina-semanal semana 2           → semana 2 do mês atual
/rotina-semanal semana 2 junho     → semana 2 de junho
/rotina-semanal semana 2 junho 2026 → explícito
```

Gera 4 arquivos em `conteudo/[ANO]/[MES]/semana-[N]/`:

| Arquivo | O que contém |
|---|---|
| `posts-estaticos.md` | Texto completo de 3–4 posts de imagem estática (legenda + hashtags + CTA) |
| `carrossel.md` | Roteiro slide a slide de 1–2 carrosséis (capa + slides + CTA final) |
| `scripts-stories-reels.md` | Scripts de 2–3 stories e 1–2 reels (cena a cena, fala, legenda, trilha sugerida) |
| `posts-simples-canva.md` | Frases curtas prontas para copiar em posts simples no Canva (frase + cor sugerida + formato) |

---

### 4. `/rotina-design` — Após a semanal
Cria os designs diretamente no Canva, prontos para editar e publicar.

```
/rotina-design                      → gera para a semana atual
/rotina-design semana 2 maio        → semana 2 de maio
/rotina-design semana 2 maio 2026   → explícito
```

Gera: `conteudo/[ANO]/[MES]/semana-[N]/designs/links-canva.md`
(com os links diretos de cada design no Canva)

---

## Máquina de Vendas — Framework de Operação

Todo mês e toda semana operam dentro de três engrenagens. Ao gerar conteúdo, sempre identifique em qual engrenagem a semana está:

### BASAL (toda semana)
Ações recorrentes para garantir o piso de receita: ISCAA (conteúdo isca), Dia V (dia fixo de venda — toda quinta), Sessão Clareza Online (call gratuita → consulta paga), Sessão Clareza em Áudio (áudio estratégico no WhatsApp), Tráfego Pago, Parcerias, Google Meu Negócio. O conteúdo semanal deve sempre alimentar pelo menos o ISCAA e o Dia V.

### PICO (semanas específicas no calendário)
Campanhas de aceleração com aquecimento + janela de venda + oferta com prazo. Formatos: Desafio WhatsApp, Desafio IG fechado, Maratona de lives, Imersão fechada, Minicurso. O conteúdo da semana PICO é 100% focado em conversão.

### OPERAÇÃO LIMPA MESA (semanas específicas no calendário)
Recuperação de leads quentes que não compraram. Funil de pressão no WhatsApp com argumento sazonal. O conteúdo da semana apoia a reativação com prova social e quebra de objeções.

### Calendário de eventos especiais (além do Basal semanal):
| Mês | Semana especial | Tipo |
|-----|----------------|------|
| Janeiro | Semana 2 | PICO |
| Janeiro | Semana 4 | LIMPA MESA |
| Março | Semana 2 | PICO |
| Abril | Semana 4 | LIMPA MESA |
| Maio | Semana 2 | PICO |
| Junho | Semana 1 | Estirão de Crescimento (topo de funil intenso) |
| Julho | Semana 2 | PICO |
| Julho | Semana 4 | LIMPA MESA |
| Setembro | Semana 1 | PICO |
| Outubro | Semana 4 | PICO |
| Novembro | Semana 1 | LIMPA MESA |
| Dezembro | Semana 1 | Estirão de Crescimento |

---

## Regras Gerais para Geração de Conteúdo

1. **Nunca invente dados ou estatísticas** sem indicar que é exemplo.
2. **Sempre respeite o tom de voz** definido na seção Identidade da Marca.
3. **Cada post deve ter um único objetivo** — não misture topo e fundo de funil no mesmo texto.
4. **CTAs devem ser específicos** — "clique no link da bio" ou "responda aqui" em vez de "saiba mais".
5. **Reels e stories têm ritmo** — escreva em frases curtas, pausas marcadas com `[pausa]`, textos de tela em CAPS.
6. **Posts simples para Canva** devem ter no máximo 10 palavras visíveis — o que sobra vai na legenda.
7. **Proibição de Lives/Ao Vivo**: Nunca sugira lives, webinars ou eventos ao vivo. Substitua por: Desafio WhatsApp (5 dias), Desafio IG Fechado (Close Friends), Série de Conteúdo Intensivo (Reels/Carrosséis) ou Minicurso Gravado.
8. **Identidade Visual**: Paleta cream (#F4EFE4), marrom escuro (#2B1A10), ouro (#C9A435). Tipografia Georgia. Emojis permitidos: ⚜️✅❤️😉🧠💪🎁🗝️🔓📆📋📌🥗. Tamanho dos posts: 2160×2700px (proporção 4:5 — post normal do Instagram em alta resolução).
9. **Regras de Slide**: Sem travessões e sem emojis no texto dos slides. Partir sempre da experiência vivida da mulher antes da explicação clínica.
10. Ao salvar um arquivo, confirme no chat qual arquivo foi salvo e o caminho completo.
