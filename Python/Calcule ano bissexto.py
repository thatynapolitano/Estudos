# Descobrir se um ano é bissexto.
# Divisível por 4, exceto se for divisivel por 100 mas não 400.
# Divisivel por 4? Sim. 
# Divisivel por 100? Não. 
# Divisível por 400? Sim. 

ano = int(input("Digite um ano:"))

if ano %4 == 0 and ano %100 != 0:
    print("Sim, o ano é bissexto")
elif ano %400 == 0 and ano %100 != 0: 
    print("Sim, o ano é bissexto")
else: 
    print("Não é bissexto")

#Outra forma
ano = int(input("Digite um ano:"))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print("Sim, o ano é bissexto")
else:
    print("O ano não é bissexto")

#Forma mais simples ainda

ano = int(input("Digite um ano:"))

if ano %400 ==0:
    print("É bissexto")
elif ano %100==0:
    print("Não é bissexto")
elif ano %4==0: 
    print("É bissexto")
else:
    print("Não é bissexto")

#Código com biblioteca

from calendar import isleap

year = int(input('Digite o ano: '))

if isleap(year):
  print('Esse ano é bissexto!')
else: 
  print('Esse ano não é bissexto!')