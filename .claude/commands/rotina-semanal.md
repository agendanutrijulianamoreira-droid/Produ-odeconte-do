Execute a Rotina Semanal de produção de conteúdo.

## Passos obrigatórios

1. Leia o arquivo `CLAUDE.md` — especialmente **Identidade da Marca**, **Máquina de Vendas** e **Regras Gerais**.
2. Determine semana, mês e ano a partir de `$ARGUMENTS`. Exemplos válidos:
   - `semana 2` → semana 2 do mês atual
   - `semana 2 junho` → semana 2 de junho do ano corrente
   - `semana 2 junho 2026` → explícito
   - Se vazio → use a semana atual baseado na data de hoje
3. Verifique se `conteudo/$ANO/$MES/editorial-mensal.md` existe. Se não existir, pare e instrua a rodar `/rotina-mensal` primeiro.
4. Leia `conteudo/$ANO/$MES/editorial-mensal.md` e `conteudo/$ANO/$MES/funil-conteudo.md`.
5. Identifique no editorial:
   - Mini-tema da semana
   - Foco no funil (Topo / Meio / Fundo)
   - Tipo da semana: **Basal**, **PICO**, **LIMPA MESA** ou **Estirão de Crescimento**
   - Posts planejados e suas intenções
6. Leia `prompts/rotina-semanal.md` para seguir a estrutura exata de cada arquivo.
7. Verifique se os arquivos da semana já existem. Se sim, pergunte antes de sobrescrever.
8. Gere os 4 arquivos respeitando:
   - **Nenhum formato de live** — substituir por Reel gravado, Carrossel, Série de Stories ou Desafio fechado
   - Em semana **PICO**: conteúdo 100% focado em conversão, com sequência diária de aquecimento → oferta → urgência
   - Em semana **LIMPA MESA**: posts de prova social e quebra de objeção que suportam a reativação por WhatsApp
   - Em semana **Estirão**: conteúdo de topo de funil puro, máximo alcance, sem oferta direta
   - Em semana **Basal**: equilibrar ISCAA (topo) + educação (meio) + pelo menos 1 CTA direto (Dia V)
9. Salve os 4 arquivos em `conteudo/$ANO/$MES/semana-$N/`:
   - `posts-estaticos.md`
   - `carrossel.md`
   - `scripts-stories-reels.md`
   - `posts-simples-canva.md`
10. Faça commit com a mensagem: `feat: conteúdo semana $N $MES $ANO`
11. Confirme no chat os 4 caminhos salvos e um resumo do calendário de publicação da semana.

## Como usar
`/rotina-semanal` → gera a semana atual
`/rotina-semanal semana 2` → semana 2 do mês atual
`/rotina-semanal semana 2 junho` → semana 2 de junho
`/rotina-semanal semana 2 junho 2026` → explícito
