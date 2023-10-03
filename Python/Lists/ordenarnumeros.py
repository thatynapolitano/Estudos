# Ordenar numeros em ordem crescente 
# O usuário precisa dar 4 números para compor a lista 

def ordenar():
    num_1 = int(input("Numero 1: "))
    num_2 = int(input("Numero 2: "))
    num_3 = int(input("Numero 3: ")) 
    num_4 = int(input("Numero 4: ")) 

    numeros = [num_1, num_2, num_3, num_4]
    ordenados = [] 

    for numero in numeros: 
        if num_1 and num_2 and num_3 and num_4:
            ordenados.append(numero)

    ordenados.sort()
    print(ordenados)

ordenar()

######### Outra forma de resolver sem usar o método sort(), apenas a lógica ############
def ordenacao():
    numeros = []

    for numero in range(4):
        numero = int(input("Digite um número: "))
        for chave, valor in enumerate(numeros):
            if numero < valor:
                numeros.insert(chave, numero)
                break
        else:
            numeros.append(numero)
        print("Lista atual:", numeros)