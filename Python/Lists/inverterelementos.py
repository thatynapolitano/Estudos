my_list = [10, 1, 8, 3, 5]
 
my_list[0], my_list[4] = my_list[4], my_list[0]
 
print(my_list)

my_list[1], my_list[3] = my_list[3], my_list[1]
 
print(my_list)

# Essa forma de inverter elementos de uma lista parece eficaz, mas apenas quando temos poucos elementos.
# Ainda será aceitável fazer dessa forma com uma lista de 100 elementos? Não.
# Você pode usar o loop for para fazer a mesma coisa automaticamente, independentemente do comprimento da lista? Sim, você pode.

length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
 
print(my_list)
 
"""
Nota:

atribuímos a variável length com o comprimento da lista atual (isso torna nosso código um pouco mais claro e mais curto)
lançamos o loop for para percorrer length//2 vezes (isso funciona bem para listas com comprimentos pares e ímpares, porque quando a lista contém um número ímpar de elementos, o meio permanece intocado)
trocamos o i-ésimo elemento (do início da lista) pelo elemento com um índice igual a (length - i - 1) (do fim da lista); no nosso exemplo, para i igual a 0 o (length - i - 1) dá 4; para i igual a 1, dá 3 - isso é exatamente o que precisávamos.
As listas são extremamente úteis, e você as encontrará com frequência.

"""