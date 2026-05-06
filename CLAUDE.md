# Sistema de Produção de Conteúdo

Este repositório é o cérebro da produção de conteúdo. O Claude executa rotinas periódicas para gerar estratégia anual, editorial mensal e posts semanais prontos para publicar ou editar no Canva.

---

## Identidade da Marca

> Preencha esta seção antes de rodar qualquer rotina.

```
NOME:           Juliana Moreira — Nutricionista

NICHO:          Nutrição para mulheres com desregulação hormonal (SOP, endometriose,
                candidíase e miomas), com foco em emagrecimento sem efeito sanfona,
                redução de inchaço e melhora de energia.

PÚBLICO-ALVO:   Mulheres de 30 a 45 anos, empreendedoras, com rotina intensa.
                Já tentaram dieta e falharam. Sofrem com compulsão noturna e ansiedade.
                Sentem inchaço constante e baixa energia. Têm dificuldade de manter constância.

DORES:          - Não conseguem emagrecer de forma consistente
                - Inchaço abdominal diário
                - Cansaço mesmo dormindo
                - Perda de controle alimentar à noite
                - Sintomas hormonais desregulados

DESEJOS:        - Emagrecer sem restrição extrema
                - Ter energia ao longo do dia
                - Sentir o corpo leve e desinchado
                - Regular hormônios e ciclo
                - Ter controle sobre a alimentação

TRANSFORMAÇÃO:  De exausta, inchada e presa em ciclos de dieta
                → Leve, regulada e no controle do próprio corpo

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
