## 1 Forma Normal 

- Definição: todos os domínios básicos apresentam valores atômicos, ou seja, não armazenam grupos repetitivos. 
- Vamos eliminar as repetições.

- Cada tupla deeve ter um identificador único
    - Solução: criar atributo ID
- Cada tupla de dados deve conter dados atômicos (não repetitivos)
    - Criar relações para os dados que se repetem.

## 2 Forma Normal

- Definição: todos os atributos não-chaves apresentam dependência total da chave primária (e não de apenas parte dela). 
- Deve estar na 1 forma normal. 
Ou seja se não tiver chave-composta está na segunda forma normal!

## 3 Forma Normal
- Definição: todos os atributos não-chaves são independentes entre si (Ausência de atributo dependente de outros atributos que não sejam chaves na relação)
- Vamos remover ou realocar os atributos que derivam de outros dados
- Remover campos de "total" e outros cálculos
- Realocar atributos em novas relações quando eles não são dependentes apenas da chave primária.
