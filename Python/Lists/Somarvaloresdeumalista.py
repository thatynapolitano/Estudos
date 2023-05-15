"""
Vamos supor que você deseja calcular a soma de todos os valores armazenados na lista my_list.

Você precisa de uma variável cuja soma seja armazenada e inicialmente atribuído um valor de 0 - seu nome será total (Nota: não vamos nomear sum pois o Python usa o mesmo nome para uma de suas funções internas: sum(). Usar o mesmo nome geralmente seria considerado uma má prática.) Em seguida, adicione todos os elementos da lista usando o loop for. Dê uma olhada no snippet no editor.

Vamos comentar sobre este exemplo:

a uma lista é atribuída uma sequência de cinco valores inteiros;
a variável i recebe os valores 0, 1, 2, 3 e 4, e depois indexa a lista, selecionando os elementos subsequentes: o primeiro, o segundo, o terceiro, o quarto e o quinto;
cada um desses elementos é adicionado pelo operador += à variável total , fornecendo o resultado final no final do loop;
observe a maneira como a função len() foi empregada - ela torna o código independente de quaisquer alterações possíveis no conteúdo da lista.
"""

my_list = [10, 1, 8, 3, 5]

total = 0

for i in range(len(my_list)):

  total += my_list[i]

print(total)

## Outra forma de fazer, sem o length 
my_list = [10, 1, 8, 3, 5]
total = 0
 
for i in my_list:
    total += i
 
print(total)

"""
O que acontece aqui?

a instrução for especifica a variável usada para navegar pela lista (i aqui) seguida pela palavra-chave in e o nome da lista que está sendo processada (my_list aqui)
a variável i recebe os valores de todos os elementos da lista subsequente, e o processo ocorre quantas vezes houver elementos na lista;
isso significa que você usa a variável i como uma cópia dos valores dos elementos e não precisa usar índices;
a função len() também não é necessária.

"""