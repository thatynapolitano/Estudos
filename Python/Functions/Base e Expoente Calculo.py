# Criar uma função potencia que recebe uma base e um expoente e calcula a potencia.

def potencia (base,expoente): # base 9 expoente 5
    resp=0
    for i in range(expoente):
        result*= base
    return result 

numa = float(input("Digite a base: "))
numb = int(input("Digite o expoente: "))

resultado = potencia(numa, numb)
print(resultado)

## Definindo uma função de potencia para colocar no calculo de potencia da minha função calcVolume 

import math 

def potencia(base,expoente): #base 9 expoente 5 => 9*9*9*9*9
  
  result = 1
  for i in range(expoente):
    result *= base #1*9 => 9 => 27 => 723
  return result

def calcVolume(raio):
  volume = (4*math.pi/3) * potencia(raio,3)
  return volume

raio = int(input('Digite o raio: '))
result = calcVolume(raio)
print(result)