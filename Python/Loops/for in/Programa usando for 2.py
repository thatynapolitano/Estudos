# Faca um programa que o usuario informa a quantidade de numeros que vai digitar. Entao tire a media desses numeros.

qtd = int(input('Digite a quantidade total de valores: '))
somatorio = 0

for i in range(qtd):
    num = float(input('Digite um valor: '))
    somatorio += num
media = somatorio / qtd
print('Media: ', media)