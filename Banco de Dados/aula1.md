## Por que utilizar (ou não) banco de dados? 

Utilizar um banco de dados é vantajoso pela organização estruturada dos dados, garantia de consistência e integridade, segurança robusta, facilidades de backup e recuperação, controle de concorrência, e escalabilidade. Ele também proporciona métodos eficientes de consulta, como SQL. No entanto, em situações de simplicidade, onde o custo e a sobrecarga de gerenciamento são preocupações, ou onde desempenho e flexibilidade são críticos, alternativas como arquivos simples ou soluções personalizadas podem ser mais adequadas. A decisão deve ser baseada nas necessidades específicas da aplicação e na complexidade dos dados.

Objetivos da Aula: 

- Compreender aspectos principais dos Sistemas Gerenciadores de Banco de Dados;
- Compreeender aspectos principais de modelagem de dados 


## SGBD

Um Sistema de Gerenciamento de Banco de Dados (SGBD) é um software projetado para definir, criar, manipular e gerenciar bases de dados. Ele proporciona uma interface entre os usuários e as bases de dados, permitindo que os dados sejam armazenados, modificados e extraídos de forma eficiente e organizada.

## Qual a diferença entre SGBD X Banco de dados? 

### <u>SGBD (Sistema de Gerenciamento de Banco de Dados)</u>

Definição: Um SGBD é um software ou um conjunto de programas que permite criar, gerenciar e manipular bancos de dados. Ele oferece ferramentas e interfaces para a definição, inserção, atualização, exclusão e consulta de dados armazenados em um banco de dados.

Funções: O SGBD fornece funcionalidades como controle de acesso, segurança, integridade dos dados, backup e recuperação, controle de concorrência e facilidades de manutenção e administração.

Exemplos: MySQL, PostgreSQL, Oracle, Microsoft SQL Server, MongoDB.

### <u> Banco de Dados </u>

Definição: Um banco de dados é uma coleção organizada de dados que é armazenada e acessada eletronicamente. Ele pode ser visto como um repositório de dados onde as informações são estruturadas de maneira que possam ser facilmente recuperadas, gerenciadas e atualizadas.

Função: O banco de dados contém os dados reais. Ele armazena informações de forma estruturada (como tabelas em um banco de dados relacional) ou de forma não estruturada/semi-estruturada (como documentos JSON em um banco de dados NoSQL).

Exemplos: As tabelas e registros armazenados em um banco de dados MySQL, os documentos armazenados em um banco de dados MongoDB.

### <i> <span style=color:pink> Resumo da Diferença </span> 
SGBD: É o software que gerencia e interage com os bancos de dados.
Banco de Dados: É a coleção de dados que é gerenciada pelo SGBD.