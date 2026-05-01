Gera os PDFs de design para a semana especificada em $ARGUMENTS.

## Passos obrigatórios

1. Determine semana, mês e ano a partir de `$ARGUMENTS` (ex: "semana 1 maio 2026"). Se vazio, use a semana atual.
2. Verifique se `conteudo/$ANO/$MES/semana-$N/carrossel.md` existe. Se não existir, instrua a rodar `/rotina-semanal` primeiro.
3. Leia os arquivos de conteúdo da semana (`posts-estaticos.md`, `carrossel.md`, `posts-simples-canva.md`).
4. Crie a pasta `conteudo/$ANO/$MES/semana-$N/designs/` se não existir.
5. Gere os 3 arquivos JSON de slides:
   - `designs/carrossel.json` — slides do carrossel (tipo capa + conteudo × N + texto + cta)
   - `designs/posts-estaticos.json` — cada post estático como 1 slide (tipo capa ou cta)
   - `designs/posts-canva.json` — cada post Canva como 1 slide (tipo capa)
6. Para cada JSON, execute:
   ```
   python3 scripts/gerar-slides.py designs/<arquivo>.json designs/<nome>.pdf
   ```
7. Confirme no chat os 3 PDFs gerados com caminho completo.

## Regras de design (sempre respeitar)
- Handle: @nutridamulhermoderna
- Nome: Juliana Moreira | Nutricionista | 2026
- Fundo limpo (#FAF8F4) — slides lisos para editar depois
- Itálico dourado (#B08A6A) para palavras de destaque na capa
- Proporção 4:5 (1080×1350px)
- Sem imagens geradas — apenas tipografia e layout limpo

## Tipos de slide disponíveis (para o JSON)
- `capa` → `label` + `titulo` (com `<em>` para dourado/itálico)
- `conteudo` → `numero` + `titulo` + `texto`
- `texto` → `titulo` + `texto` (sem número)
- `cta` → `tag` + `titulo` + `instrucao` + `cta`

## Como usar
`/rotina-design` → gera para a semana atual
`/rotina-design semana 2 maio` → gera semana 2 de maio
