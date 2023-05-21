#Exercício 6- Leia uma string e um número N. Imprima as N primeiras letras do nome digitado. Caso N seja maior do que o tamanho do nome imprima uma mensagem de erro e encerre o programa sem fazer nada

nome = input('Digite um nome: ')
N = int(input('Digite a qtd de letras: '))
tam = len(nome)

if N > tam:
    print("O nome não possui tantas letras assim...")
else: 
    for i in range(N):
     print(nome[i])
    