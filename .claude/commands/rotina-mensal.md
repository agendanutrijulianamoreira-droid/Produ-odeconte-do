Execute a Rotina Mensal de produção de conteúdo.

## Passos obrigatórios

1. Leia o arquivo `CLAUDE.md` — especialmente **Identidade da Marca** e **Máquina de Vendas**.
2. Determine mês e ano: use `$ARGUMENTS` se fornecido (ex: "maio 2026" ou "junho"). Se não, use o mês atual.
3. Verifique se `estrategia/$ANO/linha-editorial-anual.md` existe. Se não existir, pare e instrua o usuário a rodar `/rotina-anual` primeiro.
4. Leia `estrategia/$ANO/linha-editorial-anual.md` — identifique:
   - Tema central do mês
   - Produto em foco
   - Qual semana é PICO, LIMPA MESA ou Estirão de Crescimento
5. Leia `prompts/rotina-mensal.md` para seguir a estrutura de output.
6. Verifique se os arquivos do mês já existem. Se sim, pergunte antes de sobrescrever.
7. Gere os dois arquivos do mês respeitando:
   - Nenhum formato de live — usar Desafio WhatsApp, Desafio IG Fechado, Série de Conteúdo Intensivo ou Minicurso Gravado
   - O tipo de cada semana (Basal / PICO / LIMPA MESA) deve estar explícito no breakdown
8. Salve:
   - `conteudo/$ANO/$MES/editorial-mensal.md`
   - `conteudo/$ANO/$MES/funil-conteudo.md`
9. Crie as subpastas da semana se não existirem: `semana-1/`, `semana-2/`, `semana-3/`, `semana-4/`
10. Faça commit com a mensagem: `feat: editorial e funil $MES $ANO`
11. Confirme no chat os dois caminhos salvos.

## Como usar
`/rotina-mensal` → usa o mês atual
`/rotina-mensal junho` → gera junho do ano corrente
`/rotina-mensal junho 2026` → gera junho 2026
