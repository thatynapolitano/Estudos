"""
Exercício 3- Faça uma função chamada quadrado(lado) que recebe como parâmetro um número representando a medida do lado de um quadrado e imprima 3 valores:

Área (lado * lado)

perímetro (4 * lado)

tamanho da diagonal ( lado * √ 2)
"""

import math

lado = float(input("Escreva a medida do lado de um quadrado: "))

def quadrado(lado):
    area = lado * lado
    perimetro = 4 * lado 
    tam_diagonal = lado * math.sqrt(2)
    print(f"A área do quadrado é: {area}")
    print(f"O perímeto do quadrado é: {perimetro}")
    print(f"O tamanho da diagonal é: {tam_diagonal}")

quadrado(lado)


