# E-mail
Se não for possível usar um servidor SMTP, você pode dizer a Django que escreva
os emails no console adicionando a seguinte configuração no arquivos settings.py
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Full-Text Search

A pesquisa full-text é um processo custoso. Se estiver pesquisando
em mais de algumas centenas de linhas, você deve definir um índice
funcional correspondente ao vetor de pesquisa que você estiver usando.
Django disponibiliza um campo SearchVectorField para os seus modelos.

# Stemming e classificação dos resultados

Stemming (stemização) é o processo de reduzir as palavras ao seu formato de
radical (stem) ou base. O stemming é usado pelas ferramentas de pesquisa para
reduzir as palavras indexadas aos seus radicais e permitir a correspondência de
palavras flexionadas ou derivadas. Por exemplo, "música" e "músico" podem ser
consideradas palavras semelhantes por uma ferramenta de pesquisa.

# Pesquisando com semelhanças por triagramas

Outra abordagem de pesquisa é a semelhança por triagramas. Um triagrama é um
grupo de três caracteres consecutivos. Podemos avaliar a semelhança de duas strings
contando o número de triagramas que elas compartilham. Com efeito, essa abordagem
é muito eficaz para avaliar a semelhança entre palavras em vários idiomas.

Para usar triagramas no PostgreSQL, é necessário instalar antes a extensção pg_trgm.

~~~~sql
CREATE EXTENSION pg_trgm;
~~~~