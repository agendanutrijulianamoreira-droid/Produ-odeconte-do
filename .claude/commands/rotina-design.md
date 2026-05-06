Cria os designs da semana diretamente no Canva.

## Passos obrigatórios

1. Determine semana, mês e ano a partir de `$ARGUMENTS` (ex: "semana 1 maio 2026"). Se vazio, use a semana atual.
2. Verifique se `conteudo/$ANO/$MES/semana-$N/carrossel.md` existe. Se não existir, instrua a rodar `/rotina-semanal` primeiro.
3. Leia os arquivos de conteúdo da semana:
   - `conteudo/$ANO/$MES/semana-$N/carrossel.md`
   - `conteudo/$ANO/$MES/semana-$N/posts-estaticos.md`
   - `conteudo/$ANO/$MES/semana-$N/posts-simples-canva.md`
4. Use a ferramenta `list-brand-kits` do Canva para verificar se existe um brand kit disponível. Se sim, use-o em todos os designs.
5. Crie os designs no Canva usando a ferramenta `generate-design` com `design_type: "instagram_post"` para cada bloco de conteúdo:

   **A) Carrossel** — 1 design por slide do carrossel.md:
   - Para cada slide (capa + conteúdo + CTA), crie um `instagram_post` separado
   - Query: descreva o slide com título, texto e identidade visual: fundo cream (#F4EFE4), texto marrom escuro (#2B1A10), destaques em ouro (#C9A435), tipografia Georgia, tamanho 1080×1350px (proporção 4:5)
   - Sem imagens — apenas tipografia e layout limpo

   **B) Posts Estáticos** — 1 design por post em posts-estaticos.md:
   - Para cada post, crie um `instagram_post`
   - Inclua o texto principal e o CTA na query
   - Mesma identidade visual acima

   **C) Posts Canva** — 1 design por frase em posts-simples-canva.md:
   - Para cada frase curta, crie um `instagram_post` com a frase centralizada
   - Fundo na cor sugerida no arquivo (ou #F4EFE4 por padrão)
   - Texto em no máximo 10 palavras visíveis

6. Para cada design gerado, use `create-design-from-candidate` para salvar no Canva e obter o link.
7. Salve os links em `conteudo/$ANO/$MES/semana-$N/designs/links-canva.md` no formato:
   ```
   # Links Canva — Semana $N $MES $ANO

   ## Carrossel
   - Slide 1: [link]
   - Slide 2: [link]
   ...

   ## Posts Estáticos
   - Post 1 — [título]: [link]
   ...

   ## Posts Canva
   - Frase 1: [link]
   ...
   ```
8. Faça commit com a mensagem: `feat: designs canva semana $N $MES $ANO`
9. Confirme no chat os links gerados e oriente a abrir cada um no Canva para editar se necessário.

## Identidade visual (sempre respeitar)
- Fundo: #F4EFE4 (cream)
- Texto principal: #2B1A10 (marrom escuro)
- Destaque/ouro: #C9A435
- Tipografia: Georgia
- Proporção: 4:5 — 1080×1350px (equivalente a 2160×2700px em alta resolução)
- Handle: @nutridamulhermoderna
- Nome: Juliana Moreira | Nutricionista | 2026
- Sem imagens geradas — apenas tipografia e layout limpo

## Como usar
`/rotina-design` → gera para a semana atual
`/rotina-design semana 2 maio` → gera semana 2 de maio
`/rotina-design semana 2 maio 2026` → explícito
