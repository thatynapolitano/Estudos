#valor com 3 dígitos.
num = int(input('Digite um valor com 3 dígitos: '))
while num <100 or num>999:
  print('Erro!')
  num = int(input('Digite um valor com 3 dígitos: '))
print('O valor digitado foi:',num)