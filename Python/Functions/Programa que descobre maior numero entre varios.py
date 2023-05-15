#Descubra o maior valor entre uma quantidade qualquer de valores

val = int(input('Digite um valor: '))
maximo=val  # o valor maximo vai ser o maior val 
while val != 0 :  #digitou zero o programa para
  if val > maximo: # se o valor for maior que maximo 
    maximo=val # substitui o valor de máximo pelo valor passado pelo usuario. 
  val = int(input('Digite um valor: ')) # Sendo assim, pede outro valor a ser dado pelo usuario.
print('Valor máximo',maximo)  