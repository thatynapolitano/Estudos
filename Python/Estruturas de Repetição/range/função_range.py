# Range é uma função built-in do Python, ela é usada para produzir uma sequência de números inteiros a partir de um início (inclusivo) para um fim (exclusivo). Se usarmos range(i,j) será produzido:
#i, i+1, i+2, i +3..., j-1
# Ela recebe 3 argumentos:  start(opcional), stop (obrigatório) e step (opcional).

lista = list(range(4))
print(lista)

for numero in range (0,11):
    print(numero, end=" ")

for numero in range (0,51,5): #start(opcional), stop (obrigatório) e step (opcional).
    print(numero, end=" ")
