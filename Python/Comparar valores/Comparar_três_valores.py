#Escrever um programa que lê um conjunto de 3 valores. Imprima uma mensagem dizendo se os valores estão:
#"Em ordem crescente", "em ordem decrescente" ou "fora de ordem"

x = float(input("Insira um valor: "))
y = float(input("Insira um valor: "))
z = float(input("Insira um valor: "))

if x > y > z: 
    print("Os valores estão em ordem decrescente")
elif x < y < z:
    print("Os valores estão em ordem crescente")
else: 
    print("Os valores estão fora de ordem")

