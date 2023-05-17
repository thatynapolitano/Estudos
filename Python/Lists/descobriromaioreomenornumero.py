#Exercicio para descobrir o maior e o menor número em uma lista 

listaNum = [3, -5, 8, 9, -1, -9]

#Defini o primeiro valor como maior e menor:
maiorNum = listaNum[0]
menorNum = listaNum[0]

for num in listaNum:
    if num > maiorNum:
        maiorNum = num
    elif num < menorNum:
        menorNum = num
print(f"O maior número é: {maiorNum} e o menor número é: {menorNum}")