Execute a Rotina Anual de produção de conteúdo.

## Passos obrigatórios

1. Leia o arquivo `CLAUDE.md` — especialmente a seção **Identidade da Marca** e o framework **Máquina de Vendas**.
2. Se o argumento `$ARGUMENTS` contiver um ano, use-o. Caso contrário, use o ano atual baseado na data de hoje.
3. Verifique se `estrategia/$ANO/linha-editorial-anual.md` já existe. Se existir, pergunte ao usuário se quer sobrescrever antes de continuar.
4. Leia o arquivo `prompts/rotina-anual.md` para seguir a estrutura de output.
5. Gere a Linha Editorial Anual completa para o ano definido, respeitando:
   - Identidade da marca definida no CLAUDE.md
   - Framework Basal / Pico / Limpa Mesa
   - Calendário de campanhas do framework Máquina de Vendas
   - Nenhum formato de live — substituir por Desafio WhatsApp, Desafio IG Fechado, Minicurso Gravado ou Série de Conteúdo Intensivo
6. Salve o resultado em `estrategia/$ANO/linha-editorial-anual.md`.
7. Faça commit com a mensagem: `feat: linha editorial anual $ANO`
8. Confirme no chat: "Linha editorial anual $ANO salva em `estrategia/$ANO/linha-editorial-anual.md`."

## Como usar
`/rotina-anual` → usa o ano atual
`/rotina-anual 2027` → gera para 2027
