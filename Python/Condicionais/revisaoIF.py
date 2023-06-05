#Revisão IF

nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')
#len => length => retorna a qtd de itens/caracteres na lista/string 
if len(nome1) > len(nome2):
  print('O primeiro nome possui mais letras')
elif len(nome2) > len(nome1):
  print('O segundo nome possui mais letras')
else:
  print('Ambos são iguais')

  