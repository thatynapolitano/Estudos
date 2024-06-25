# Acolhimento conceitual

- Quais comandos SQLs vocês já conhecem? 
- Referência para comandos: <br>
    https://www.w3schools.com/sql/sql_ref_keywords.asp  

## Objetivo da Aula
- Conhecer os comandos SHOW, USE e DESCRIBE
- Conhecer mais a fundo as restrições das chaves primárias e estrangeiras
- Conhecer o comando de inserção INSERT 

## Comando SHOW 
- Lista os bancos de dados existentes nesta conexão 

show databases; 

## Comando USE
- USE < nome do banco >;
    - Marca o BD como em uso 

## Comando DESCRIBE
- DESCRIBE < tabela >;
    - Mostra os campos da tabela (metadados!)

## Chaves e restrições
Na criação do banco de dados é preciso colocar restrições. Se um usuário tentar deletar/atualizar algo qual tipo de restrição retornará.

- DEFAULT: define um valor padrão
![alt text](assets/image-48.png)
- É uma restrição, pode ser removida
![alt text](assets/image-49.png)

- Restrições de integridade
    - Existe apenas nas chaves estrangeiras

![alt text](assets/image-50.png) 

Os camandos ON DELETE e ON UPDATE ocorrem em conjunto com os comandos abaixo:

- ON DELETE: ao excluir
- ON UPDATE: ao atualizar
-  ++++ 
- CASCADE: atualiza/apaga em cascata 
- NO ACTION: não faz nada e acusa erro
- RESTRICT: não faz nada e acusa erro 
- SET NULL: marca como nulo 


<br>

- UNIQUE KEY: restrição de unicidade
    - Mas na prática é um índice
Diferença para a PRIMARY KEY?
- Não identifica o registro, apenas não se repete (tipo CPF, numero CNH, endereço de e-mail, código de produto...)
- Pode haver mais de uma UK (Unique Key) por tabela

![alt text](assets/image-51.png) 

![alt text](assets/image-52.png) 


CREATE TABLE Usuarios ( <br>
    id INT PRIMARY KEY, <br>
    nome VARCHAR(100), <br>
    cpf CHAR(11) UNIQUE <br>
);

- AUTO INCREMENT: incremento automático 
    - Sempre é UNSIGNED (sem sinal = positivo)
    - Normalmente em primary key (ID)

![alt text](assets/image-53.png) 

## Comando INSERT
- INSERT: Insere dados no BD
- Regras: 
    - Valores do tipo caractere entre aspas simples
    - Datas entre aspas simples e no formato AAAA-MM-DD
    - Valores numéricos sem aspas
    - Pode usar NULL se o campo permitir

![alt text](assets/image-54.png) 
OBS: valores sempre separados por vírgula

![alt text](assets/image-55.png)

![alt text](assets/image-56.png)

![alt text](assets/image-57.png)

Precisa NOT null se eu definir um valor padrão com DEFAULT? <br>
<b> Não. </b>


![alt text](assets/image-58.png)

