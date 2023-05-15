def ehPositivo(valor):
  if valor >0:
    return True
  else:
    return False

#True, False boleanos
num = int(input('Digite um valor: '))
while num != 0:
  if ehPositivo(num) :
    print('Positivo')
  else:
    print('Não positivo')
  num = int(input('Digite um valor: '))