Gera os designs da semana — via Canva MCP (preferencial) ou PDFs locais — para a semana especificada em $ARGUMENTS.

## Antes de começar
1. Leia `prompts/rotina-design.md` para o fluxo completo e instruções de cada modo.
2. Determine semana, mês e ano a partir de `$ARGUMENTS`. Se vazio, use a semana atual.
3. Verifique se `conteudo/$ANO/$MES/semana-$N/carrossel.md` existe. Se não, instrua a rodar `/rotina-semanal`.

## Fluxo resumido

### Modo A — Canva MCP (quando conectado)
Leia `prompts/rotina-design.md` e siga a seção "Modo A" para cada design.
Templates: Carrossel `DAG-TljeV_Q`, Posts `DAG4xGMUwKw`, Brand Kit `kAEN0HquLOI`.

### Modo B — PDF local (offline)


### `editorial` — **tipo principal** (padrão para posts estáticos)
Texto corrido em 1–2 parágrafos com bold inline para ênfase. Limpo, direto, sem enfeites.
Hook obrigatório: a primeira frase já deve parar o scroll.

```json
{
  "tipo": "editorial",
  "blocos": [
    "Mulheres com SOP têm <strong>resistência à insulina</strong> mesmo sem comer mal.",
    "Isso significa que o corpo armazena gordura com muito mais facilidade. <strong>Não é falta de força de vontade. É bioquímica.</strong>"
  ]
}
```

### `frase` — hook de impacto imediato (posts simples Canva)
Uma frase grande que para o scroll + complemento opcional menor.
Use `<em>` para destaque em dourado/itálico, `<strong>` para negrito.

```json
{
  "tipo": "frase",
  "gancho": "Seu corpo não está errado. <em>O protocolo estava.</em>",
  "complemento": "A diferença entre frustração e resultado é ter um plano feito pra você."
}
```

### `capa` — abertura do carrossel
Label pequeno + título grande. Deve gerar curiosidade imediata.

```json
{
  "tipo": "capa",
  "label": "3 sinais que seu corpo está pedindo ajuda",
  "titulo": "Você ignora porque <em>parece normal</em>."
}
```

### `conteudo` — slides numerados do carrossel
Número grande decorativo + título + texto explicativo.

```json
{
  "tipo": "conteudo",
  "numero": "01",
  "titulo": "Inchaço que não passa",
  "texto": "Não é água parada. É <strong>inflamação crônica</strong> — e ela responde à alimentação."
}
```

### `destaque` — barra escura + texto (para slides de ruptura dentro do carrossel)
Barra marrom escura no topo com frase curta + parágrafo de desenvolvimento.

```json
{
  "tipo": "destaque",
  "barra": "Como foi <em>construído:</em>",
  "texto": "Com <strong>protocolo hormonal individualizado</strong>, ajustado semana a semana.",
  "rodape": "Cada peça no lugar certo."
}
```

### `cta` — chamada final para ação
Tag + título + instrução + botão.

```json
{
  "tipo": "cta",
  "tag": "Próximo passo",
  "titulo": "Quer saber o que está travando o seu corpo?",
  "instrucao": "Clique no link da bio e agende sua Sessão Clareza.",
  "cta": "Quero entender meu corpo →"
}
```

---

## Regras de conteúdo (sempre respeitar)

- **Hook nos primeiros 3 segundos**: a primeira frase de todo post `editorial` ou `frase` deve ser uma afirmação que para o scroll — específica, provocativa ou surpreendente. Nunca comece com "Você sabia que...".
- **Bold estratégico**: negrite apenas 2–4 palavras por bloco, as que carregam o peso da frase.
- **Sem travessões** no texto dos slides. Use vírgula ou ponto.
- **Sem emojis** no texto dos slides.
- **Máx. 2 parágrafos** por slide `editorial`.
- **Posts simples Canva** usam `frase` com gancho de no máximo 12 palavras.
- Identidade visual (automática via script): fundo #F5F1EB, texto #1A1209, dourado #C9A435, header e footer automáticos.

---

## Como usar
`/rotina-design` → gera para a semana atual
`/rotina-design semana 2 maio` → gera semana 2 de maio
`/rotina-design semana 2 maio 2026` → explícito
1. Leia os arquivos de conteúdo da semana.
2. Crie a pasta `conteudo/$ANO/$MES/semana-$N/designs/` se não existir.
3. Extraia os JSONs de slides de `carrossel.md`, `posts-estaticos.md`, `posts-simples-canva.md`.
4. Salve os JSONs em `designs/` e execute o script para cada um:
   ```
   python3 scripts/gerar-slides.py designs/<arquivo>.json designs/<nome>.pdf
   ```
5. Salve links Canva ou caminhos dos PDFs em `designs/links-canva.md`.
6. Confirme no chat os designs gerados com caminhos completos.

