#Dado um numero inteiro nao nulo de tres digitos, imprimir este numero ao contrario, isto eh, se a entrada for 123 (cento e vinte e tres), imprimir numero invertido.

numero = int(input("Digite um numero de 3 digitos: "))
centena = numero//100
unidade = numero%10 
dezena = numero//10%10 
print('Centena:', centena)
print('Dezena:', dezena)
print('Unidade:', unidade)
print(unidade*100 + dezena*10 + centena)


#Outra forma: 

numero = int(input("Informe um numero:"))
numero = numero[::-1]
print(numero)