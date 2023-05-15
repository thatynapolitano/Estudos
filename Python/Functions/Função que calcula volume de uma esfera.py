# Exercício 6- Faça uma função que recebe o um raio(R) e retorne o volume de uma esfera. Leitura e impressão de dados deve ser feita fora da função.

# O volume de uma esfera é fornecido pela fórmula V = (4π/3) * R3


def CalcularVolume (r):
    volume = ((4*3.14)/3) * (r**3)
    return volume 

Resultado = CalcularVolume(5)
print(Resultado)

# Usando biblioteca que tem o valor de pi 

import math 

def CalcularVolume (r):
    volume = ((4*math.pi)/3) * (r**3) 
    return volume 

Resultado = CalcularVolume(5)
print(Resultado)