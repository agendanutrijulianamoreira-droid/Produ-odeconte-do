Cria 1 peça de conteúdo isolada de forma rápida, sem precisar rodar o fluxo semanal.

## Antes de começar
1. Leia `CLAUDE.md` — seção Identidade da Marca.
2. Leia `prompts/humanizacao.md` — **obrigatório antes de entregar qualquer copy**.
3. Se existir `conteudo/$ANO/$MES/editorial-mensal.md`, leia para manter coerência com o mês.

## Como processar $ARGUMENTS

O argumento vem no formato: `[tema] [formato]`

Exemplos:
- `compulsão noturna e cortisol → carrossel`
- `por que a calça não fecha na TPM → post estático`
- `bastidor da semana → stories`
- `resultado de paciente → reel 30s`
- `Dia V de hoje → post de conversão`

Se o formato não for especificado, sugira o mais adequado ao tema antes de gerar.

## Passos

1. Identificar tema, formato e estágio de funil
2. Gerar o conteúdo completo seguindo `prompts/conteudo-rapido.md`
3. Aplicar checklist de humanização de `prompts/humanizacao.md`
4. Reescrever qualquer trecho que falhar no filtro
5. Entregar copy completa + JSON de slides (se carrossel ou post)
6. Salvar em `conteudo/$ANO/$MES/avulsos/[data]_[tema-kebab].md` se o usuário confirmar

## Como usar

```
/conteudo-rapido compulsão noturna e cortisol → carrossel
/conteudo-rapido sinal de candidíase que ninguém fala → post estático
/conteudo-rapido bastidor da semana → stories
/conteudo-rapido Dia V – Método Reino → post de conversão
```
