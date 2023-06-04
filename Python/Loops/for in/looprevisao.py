qtd = int(input('Digite a qtd de valores pares para somar: '))
soma=0 #variavel que vai somar todos os valores
num=2 #variavel que guarda o valor da vez
for i in range(qtd):
  soma +=num
  num+=2

print(f'A soma dos {qtd} primeiros valores pares deu {soma}')