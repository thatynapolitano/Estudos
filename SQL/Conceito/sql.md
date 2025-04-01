# O que é SQL?

> Structured Query Language, ou Linguagem de Consulta Estruturada ou SQL, é a linguagem de pesquisa declarativa padrão para banco de dados relacional (base de dados relacional)". 

Alguns dos seus principais elementos: 

- Comandos - executados resultam um efeito persistente sobre dados e estruturas, ou controlam transações, conexões, sessões, etc.
    - EX: SELECT, INSERT, UPDATE, DELETE, CREATE TABLE, GRANT, etc.

- Cláusulas - componentes dos comandos. Em muitos casos, alguns são opcionais.
    - EX: FROM, WHERE, GROUP BY

- Expressões - os quais produzem tanto valores escalares, como tabelas consistindo de colunas e linhas
    - Ex: A+B, A*ABS(B-20)

- Predicados - especificam condições que podem ser avaliadas pela lógica, retornando verdadeiro, falso ou desenconhecido 
    - EX: A>B, C BETWEEN 20 AND 200

- Queries - que retornam dados baseados em critérios específicos
    - EX: SELECT COLUNA FROM TABELA

| Linguagem Natural   | Spark/SQL |
| -------- | ------- |
| Número (inteiro) | Int   |
| Número (com casa decimal) | Float   |
| Texto    | String   |
| Sim/Não   | Boolean   |
| Data    | Date |
| Data - Hora    | Timestamp |
| Vazio/Nulo   | null |

