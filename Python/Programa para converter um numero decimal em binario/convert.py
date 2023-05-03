# Programa para converter um número decimal em binário 

numero=int(input('Digite um número inteiro: '))
binario=''
while numero > 0:
 binario+=str(numero%2)
 numero//=2
print(f'O binário correspondente é: {binario[::-1]}')