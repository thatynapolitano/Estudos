
# Teoria de Base
- Chaves primátias e estrangeiras 
- Especialização e generalização 
- Cardinalidade
- Modelo lógico de dados
- Restrições de integridade


## Entidade associativa
Exemplo:
Contexto: Imagine um sistema de gestão escolar que precisa rastrear quais cursos os estudantes estão matriculados e detalhes adicionais dessa matrícula.

Entidades Primárias: "Estudante" e "Curso".
Entidade Associativa: "Matrícula".
Descrição:

Estudante tem atributos como ID do Estudante, Nome, Data de Nascimento.
Curso tem atributos como ID do Curso, Nome do Curso, Créditos.
Entidade Associativa "Matrícula":

Atributos próprios: Data de Matrícula, Nota Final.
Chaves Estrangeiras: ID do Estudante (referenciando Estudante), ID do Curso (referenciando Curso).

## Instância de Entidade
É o dado que vai preencher a tabela. É o dado que estamos armazenando. 

## Chave primária
- Primary Key: "PK"
- Função: identificação única de uma instância 
    - Nunca se repete (Sem duplicados)
    - Obrigatório (Sem nulos)
    - Um ou mais atributos (a chave primária pode ser uma chave composta) Uma chave composta em um banco de dados relacional é uma chave primária que é formada por dois ou mais campos (colunas) da tabela. Essa combinação de colunas é utilizada para garantir a unicidade de cada linha na tabela, ou seja, a combinação dos valores nesses campos deve ser única em cada registro.
    - Preferencialmente numérica (desempenho)
- Chave primária composta (chave composta é sempre chave primária): é uma chave primária que consiste em dois ou mais campos (colunas) em uma tabela de banco de dados relacional. A combinação dos valores nessas colunas deve ser única para cada registro na tabela, garantindo a unicidade de cada linha.

![alt text](assets/image-28.png)

![alt text](assets/image-8.png) 

Repare que o código acima não se repete, é único. Ou seja, a instância "código" é a nossa PK.

CPF pode ser uma chave primária? 
- "Pode", mas não é interessante.
- Porém o CPF é um dado natural, um dado pessoal, por mais que seja um número único é interessante usar um dado que esteja inserido no contexto dos dados.

Quando não existir uma chave primária, é interessante criar uma:
- Surrogate key: chave substituta/artificial
- Melhor se for número
- Autoincremental (em geral)
    Ex: Código RU na Uninter.

## Chave estrangeira 
- Foreign Key: "FK"
- Campo de uma Entidade que faz referência a outra.
    - Pode repetir
    - Sempre é a chave primária da entidade referenciada
    - E se for composta?
        - Todos os campos vão na chave
        - É uma boa ideia usar chave composta como referência? Não, pois é não há economia de espaço, performance e desempenho comprometido.

- Vantagens:
    - Evita duplicidade de registros
    - Economiza espaço
    - Agiliza a busca

![alt text](assets/image-9.png)

## Especialização x Generalização
- Especialização
    - Entidade com mais informações do que a entidade principal
- Generalização
    - Entidade com apenas as informações principais que similares às especializadas

![alt text](assets/image-13.png)

# <i><span style=color:pink> Resumo </span></i> 

## Generalização
<b>Definição</b>: Generalização é o processo de abstrair características comuns de várias entidades em uma entidade mais geral (ou "superentidade").

<b>Objetivo</b>: O objetivo é identificar as semelhanças entre entidades e criar uma entidade que as represente de forma geral, de modo a reduzir a redundância e simplificar o modelo.

<b>Exemplo</b>: Considere duas entidades, "Carro" e "Moto". Ambas podem ser generalizadas em uma entidade mais geral chamada "Veículo", que contém atributos comuns como "marca", "modelo", "ano", etc.

<b>Entidades específicas</b>: Carro, Moto
<b>Entidade geral</b>: Veículo

## Especialização
<b>Definição</b>: Especialização é o processo inverso de generalização, onde uma entidade geral é dividida em entidades mais específicas que herdam os atributos da entidade geral e podem ter atributos adicionais próprios.

<b>Objetivo</b>: O objetivo é capturar as diferenças entre subgrupos de uma entidade mais geral, permitindo uma representação mais detalhada e específica dos dados.

<b>Exemplo</b>: Continuando com o exemplo anterior, a entidade "Veículo" pode ser especializada em "Carro" e "Moto", onde "Carro" pode ter atributos específicos como "número de portas" e "Moto" pode ter atributos específicos como "tipo de guidão".

<b>Entidade geral</b>: Veículo
<b>Entidades específicas</b>: Carro, Moto

## Cardinalidade
- Quantos de quem?
    - Um cliente faz quantos pedidos?
    - Um restaurante tem quantos clientes?
    - Um cliente faz um pedido em quantos restaurantes?

Um cliente pode fazer varios pedidos, entao a relacao entre uma entidade Cliente e uma entidade Pedido sera de 1 para Muitos (1-N)  (1-*). 

![alt text](assets/image-14.png)
![alt text](assets/image-15.png)
![alt text](assets/image-16.png)

![alt text](assets/image-17.png)


### Um para um (1:1)
- Chave estrangeira ficará aonde? 
    - Nesse caso, tanto faz. Posso colocar o código da pessoa no passaporte o código do passaporte na entidade da pessoa.
- Poderiam ser dados de uma mesma entidade?
    - Sim!

![alt text](assets/image-18.png) 

### Um para um (1:n)
- A chave estrangeira ficará aonde? 
    - No lado que tem N, no lado que tem muitos
- Poderiam ser dados de uma mesma entidade?
    - Não! Irá ter duplicidades e repetição de informações. Teriam muitas conquistas numa mesma entidade.

![alt text](assets/image-19.png)

![alt text](assets/image-20.png)

### Um para um (n:n)
- A chave estrangeira ficará aonde? 
    - Ficara numa entidade
    - Cria-se uma nova entidade intermediaria que se chama <i>Entidade Associativa</i> 
    - O proposito dela e fazer uma associacao entre duas entidades
- A modelagem só acaba depois que não houver mais relacionamentos n:n
- Todos os relacionamentos devem ser reduzidos a 1:1 ou 1:n 

![alt text](assets/image-21.png) 
![alt text](assets/image-22.png)
![alt text](assets/image-23.png)
![alt text](assets/image-24.png)

# Modelo Lógico 
![alt text](assets/image-25.png)

- Relações = tabela / entidades
- Tuplas = linhas da tabela / registros
- Tipos dos dados = Dominio
- Atributos - colunas / campos

![alt text](assets/image-26.png) 

## Diferenças para o modelo conceitual:

- Define o dominio dos atributos
- Define restrições de integridade

## Integridade 
![alt text](assets/image-27.png)

### Integridade de chave
- Cada registro é identificado de forma única
    - Chave primátia única não nula

### Integridade referencial 
- Toda chave estrangeira faz referência a um valor válido
- Esse valor, que é chave primária em outra relação, existe
- Portanto, não permite excluir registros (Gambiarra! Não façam, viola a integridade)

### Restrição de unicidade
- Todas as tuplas de uma relação são unicas
- Pelo menos um dos atributos deve variar de uma tupla para outra

### Restrições de atibutos e padrões
- NOT NULL: preenchimento obrigatório
- UNIQUE: impede repetição nas tuplas
- PRIMARY KEY: chave primária
    - Sempre é UNIQUE NOT NULL
- FOREIGN KEY: chave estrangeira
- CHECK: condicional (regra, ex: regras definidas para cpf. Garantia de receber CPF da forma correta) Ou uma condição booleana (campo de flag).
- DEFAULT: valor padrão (quando ninguém preencher nada, terá um valor padrão para não existir valor null)

![alt text](assets/image-29.png)

