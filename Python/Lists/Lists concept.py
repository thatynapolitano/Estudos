"""
Era uma vez um chapéu. O chapéu não continha coelhos, mas uma lista de cinco números:1, 2, 3, 4 e 5.

Sua tarefa:

- escreva uma linha de código que solicite que o usuário substitua o número do meio na lista por um número inteiro inserido pelo usuário (Etapa 1)
- escreva uma linha de código que remova o último elemento da lista (Etapa 2)
- escreva uma linha de código que imprima o comprimento da lista atual (Etapa 3).
"""

#Etapa 1 
chapeu = [1, 2, 3, 4, 5]
print(chapeu)

number = int(input("Coloque um número inteiro aqui para substituir o número do meio da lista:" )) 

chapeu[2] = number 
print(chapeu)

#Etapa 2 
del chapeu[-1]
print(chapeu)

#Etapa 3 
print("List length: " , len (chapeu))

