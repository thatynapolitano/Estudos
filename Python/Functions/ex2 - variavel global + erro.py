numeroA=12 #variavel global, todas as funções acessam

def func():
  numero=6
  print('func numero:',numero)
  print('func numeroA:',numeroA)


#código principal
func()
print('principal numeroA:',numeroA)
print('principal numero::',numero) #erro não consegue acessar dentro da func