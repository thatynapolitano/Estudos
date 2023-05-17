mercado = [['Batata', 4, 3.5], ['Laranja', 2, 4.2], ['Feijão', 1, 3.1]]
#       0     1    2
#item [nome, qtd, valor]
soma=0
print('Lista de compras:')
print('-'*20)
print('item | quantidade | valor unitário | valor total')
for item in mercado:
  print(f'{item[0]} | {item[1]} | {item[2]}  | {item[1]*item[2]}')
  soma+=item[1]*item[2]

print("-"*20)
print('Valor final:', soma)