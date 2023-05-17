#criando uma lista vazia para receber as informações
item = []
#criando uma lista vazia para receber os itens
mercado = []
#item [nome,qtd,valor]
for i in range(3): #vai repetir 3 vezes
  item.append( input('Digite o nome do item: '))
  item.append( int(input('Digite a qtd: ')))
  item.append( float(input('Digite o valor: ')))
  mercado.append(item[:])#anexando uma cópia do item
  item.clear() #esvazia a lista item
print(mercado)


