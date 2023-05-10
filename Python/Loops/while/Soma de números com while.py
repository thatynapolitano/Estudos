#Faça um programa que descubra qual a soma dos 50 primeiros números.

inicial = 0
final = 50

i=inicial 
soma=0
while i<=final:
  print(i)
  soma= soma+i
  i+=1 # i= i+1

print('valor acumulado',soma)

# Depois quero a soma apenas dos ímpares.

inicial = 0
final = 50

i=inicial 
soma=0
while i<=final:
  if i%2 != 0:
    soma= soma+i
  i+=1 # i= i+1

print('valor acumulado',soma)

# Outra forma, mais eficiente e sem o if: Ao invés de executar um por um incrementando +1, eu apenas incremento +2 no i, assim o while sempre passará por um número ímpar. 

inicial = 1
final = 50

i=inicial 
soma=0
while i<=final:
  print('valor:',i)
  soma= soma+i
  i+=2 # i= i+2

print('valor acumulado',soma)