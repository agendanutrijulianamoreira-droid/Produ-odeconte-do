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
  Recorrência:  Comunidade (R$47–97/mês)
  Conversão:    Consulta (R$200)
  Core:         Método Reino Trimestral (R$600)
  Upsell:       Acompanhamento avançado 3–6 meses (R$1.500–R$3.000+) — em breve

OBJETIVO:       Converter seguidores e leads em consulta paga e protocolos de
                acompanhamento. Meta: R$30.000/mês com previsibilidade.

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
    linha-editorial-anual.md     ← gerado pela Rotina Anual

conteudo/
  [ano]/
    [mes]/
      editorial-mensal.md        ← gerado pela Rotina Mensal
      funil-conteudo.md          ← gerado pela Rotina Mensal
      semana-1/
        posts-estaticos.md       ← gerado pela Rotina Semanal
        carrossel.md             ← gerado pela Rotina Semanal
        scripts-stories-reels.md ← gerado pela Rotina Semanal
        posts-simples-canva.md   ← gerado pela Rotina Semanal
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

## Rotina Anual — Como executar

Execute uma vez por ano (idealmente em dezembro para o ano seguinte).

**Comando:** leia o arquivo `prompts/rotina-anual.md`, siga as instruções e salve o resultado em `estrategia/[ANO]/linha-editorial-anual.md`.

O arquivo gerado contém:
- Tema/palavra-chave do ano
- Pilares de conteúdo (3–5 pilares)
- Arcos narrativos mês a mês
- Produtos a empurrar em cada trimestre
- Sazonalidades e datas relevantes do ano

---

## Rotina Mensal — Como executar

Execute no último dia ou primeira segunda-feira de cada mês.

**Pré-requisito:** `estrategia/[ANO]/linha-editorial-anual.md` deve existir.

**Comando:** leia o arquivo `prompts/rotina-mensal.md` e o arquivo de estratégia anual correspondente, gere o editorial do mês atual e salve em:
- `conteudo/[ANO]/[MES]/editorial-mensal.md`
- `conteudo/[ANO]/[MES]/funil-conteudo.md`

O editorial mensal contém:
- Tema central do mês e por que agora
- Objetivo de conversão do mês (qual produto empurrar)
- Breakdown das 4 semanas: foco de cada semana no funil (topo/meio/fundo)
- Pauta de 16–20 posts distribuídos nas semanas

O funil de conteúdo contém:
- Mapa visual em texto: quais posts atraem, engajam, convertem
- Chamadas para ação (CTAs) por etapa

---

## Rotina Semanal — Como executar

Execute toda segunda-feira (ou domingo à noite).

**Pré-requisito:** `conteudo/[ANO]/[MES]/editorial-mensal.md` deve existir.

**Comando:** leia o arquivo `prompts/rotina-semanal.md`, o editorial mensal e o funil do mês corrente. Gere os 4 arquivos da semana correspondente e salve em `conteudo/[ANO]/[MES]/semana-[N]/`.

Os 4 arquivos gerados:

| Arquivo | O que contém |
|---|---|
| `posts-estaticos.md` | Texto completo de 3–4 posts de imagem estática (legenda + hashtags + CTA) |
| `carrossel.md` | Roteiro slide a slide de 1–2 carrosséis (capa + slides + CTA final) |
| `scripts-stories-reels.md` | Scripts de 2–3 stories e 1–2 reels (cena a cena, fala, legenda, trilha sugerida) |
| `posts-simples-canva.md` | Frases curtas prontas para copiar em posts simples no Canva (frase + cor sugerida + formato) |

---

## Regras Gerais para Geração de Conteúdo

1. **Nunca invente dados ou estatísticas** sem indicar que é exemplo.
2. **Sempre respeite o tom de voz** definido na seção Identidade da Marca.
3. **Cada post deve ter um único objetivo** — não misture topo e fundo de funil no mesmo texto.
4. **CTAs devem ser específicos** — "clique no link da bio" ou "responda aqui" em vez de "saiba mais".
5. **Reels e stories têm ritmo** — escreva em frases curtas, pausas marcadas com `[pausa]`, textos de tela em CAPS.
6. **Posts simples para Canva** devem ter no máximo 10 palavras visíveis — o que sobra vai na legenda.
7. Ao salvar um arquivo, confirme no chat qual arquivo foi salvo e o caminho completo.
