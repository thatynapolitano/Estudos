#Revisão IF e ELSE
# Para criar uma estrutura condicional com dois desvios, podemos utilizar as palavras if e else. Como sabemos a expressão lógica testada no if for verdadeira, então o bloco de código do ig será executado. Caso contrário o bloco de código do else será executado.

# IF - ELIF - ELSE
# Em alguns cenários queremos mais de dois desvios, para isso podemos utilizar a palavra reservada elif. O elif é composto por uma nova expressão lógica, que será testada e caso retorne verdadeiro o bloco de código do elif será executado. Não existe um número máximo de elifs que podemos utilizar, porém evite criar grandes estruturas condicionais, pois elas aumentam a complexidade do código.


nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')
#len => length => retorna a qtd de itens/caracteres na lista/string 
if len(nome1) > len(nome2):
  print('O primeiro nome possui mais letras')
elif len(nome2) > len(nome1):
  print('O segundo nome possui mais letras')
else:
  print('Ambos são iguais')


# Outro exemplo 

conta_normal = True 
conta_universitaria = False

saldo = 2000
saque = 500 
cheque_especial = 450

if conta_normal:
  if saldo >= saque:
    print("Saque realizado com sucesso!")
  elif saque <= (saldo + cheque_especial):
    print("Saque realizado com uso do cheque especial")
elif conta_universitaria:
  if saldo >= saque:
    print("Saque realizado com sucesso!")
  else: 
    print("Saldo insuficiente!")
  