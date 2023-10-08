# 📔 Sobre NoSQL 

### O que é um Banco de Dados não relacional? 

- Termo correto: NOT Only SQL 
- Não seguem modelo de tabelas e relacionamentos
- Projetos para lidar com alto volume de dados, alta escalabilidade
- Alta flexibilidade na estrutura de dados
- Eles são amplamento utilizados em cenários onde a consistência imediata dos dados não é crítica

### ✨ Diferenças 

| SQL                 | NoSQL                      | 
| ------------------- | -------------------------- |
| Modelo de Dados Fixo| Modelos de Dados Flexível | 
| Escalabilidade vertical (hardware)| Escalabilidade horizontal |
| Transações ACID 100% | Transações ACID ausentes total ou parcial |
|Linguagem de consulta SQL |Cada SGBD tem sua própria linguagem de consulta |

### ✨ Vantagens 

- Flexibilidade na modelagem
- Alta escalabilidade
- Melhor desempenho em cenário de consulta intensiva
- Tolerância a falhas

### ✨ Desvantagens

- Menor consistência de dados imediata
- Menor suporte a consultas complexas (depende do SGBD)
- SGBD: Um sistema de Gerenciamento de Banco de Dados ou Sistema de Gestão de Bases de Dados - do inglês Data Bse Management System - é o sistema de software responsável pelo gerenciamento de um ou mais bancos de dados.

### ✨ Tipos baseados em: 
- Key-Value (chave valor)
  -  Armazena dados como pares de chave e valor, onde cada chave é um identificador único para acessar o valor correspondente.\
  **Exemplo de SGBD:** Redis, Riak, Amazon DynamoDB.\
  **Uso:** Um site pode usar um banco de dados Redis para armazenas informações de sessão de usuário.

- Documento 
  - Armazenam dados em documentos semiestruturados, geralmente em formato JSON ou BSON.\
  **Exemplo de SGBD:** MongoDB, Couchbase, Apache CouchDB.\
  **Uso:** Um catálogo de e-comeerce pode usar o MongoDB para armazenar informações de produtos, como nome, descrição, preço e atributos adicionais. 

- Coluna 
  - Armazenam dados em formato de colunas, o que permite alta escalabilidade e eficiência em determinados tipos de consultas.\
  **Exemplo de SGBD:** Apache Cassandra, ScyllaDB, HBase.\
  **Uso:** Um sistema de registro de aplicativos pode usar o Apache Cassandra para armazenar registros de log. 

- Grafos 
  - Utilizado para armazenar e consultar dados interconectados, onde os relacionamentos entre os dados são tão importantes quantos os próprios dados.\
  - **Exemplo de SGBD:** Neo4j, Amazon Neptune, JanusGraph.\
  - **Uso:** Uma rede social podeusar o Neo4j para armazenar os perfis dos usuários e suas conexões, permitindo consultas eficientes para encontrar amigos em comum.

- entre outros tipos... Citei aqui os principais, mais utilizados.

