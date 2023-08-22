#Um programa que peça a um usuário digite seu nome e um número inteiro e imprima o nome daquele usuário o número de vezes informado.

nome = input("Digite seu nome: ")
numero = int(input("Digite um número inteiro: "))

for i in range(numero):
    print(nome)
