lista = [10,15,18,22,19,21,29]

tam = len(lista)

for i in range(tam): #loop que vai de 0 até tam-1
  if lista[i] % 2 == 0 : # verifica se o valor na posição i é par
    lista[i] = 0
  else: #caso não seja par, só pode ser ímpar
    lista[i] =1

print(lista)

#Outra forma de fazer: 

lista = [10,15,18,22,19,21,29]
lista2 = []

for i in lista:
  if i %2 == 0:
    lista2.append(0) 
  elif  i %2 != 0:
    lista2.append(1) 
print(lista2)