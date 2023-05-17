megaSena = (8, 20, 37, 40, 44, 51) #tupla entre parenteses
#megaSena[4]=45   ERRO  Não podemos alterar tuplas!
print(megaSena[0])
print(megaSena[1])
print(megaSena[2])
print(megaSena[3])
print(megaSena[4])
print(megaSena[5])

# Outra forma de acessar os valores da minha tupla: 

megaSena = (8, 20, 37, 40, 44, 51)

for numero in megaSena :
  print(numero)

# Outra forma: 

megaSena = (8, 20, 37, 40, 44, 51)

tam = len(megaSena) #length(coprimento) - tamanho
for i in range(tam): #for 0-5
  print('numero sorteado',megaSena[i])

# Saber o valor e o indice

#enumerate i=indice v=valor
megaSena = (8, 20, 37, 40, 44, 51)
for pos,valor in enumerate(megaSena):
  print('Na posição',pos,'temos o valor',valor)