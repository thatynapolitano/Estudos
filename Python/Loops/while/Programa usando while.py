# Faça um programa que leia valores do teclado até o usuário digitar 0.
# No momento que o usuário digitar 0, o programa deve informar qual a média dos
# valores digitados.
# O valor 0 não deve ser incluído nesse calculo de média.

somatorio= 0 
qtd=0 

num = float(input("Digite um valor :"))

while num != 0:
    somatorio += num
    qtd += 1
    num = float(input("Digite um valor :"))

if qtd != 0:
    media = somatorio / qtd
    print("media:", media)
else: 
    print("Digite algum valor na próxima.")
