def maior3(x,y,z):
  if x >= y and x >= z :
    return x
  elif y >=x and y >=z :
    return y
  else:
    return z

val1 = float(input('Digite um valor: '))
val2 = float(input('Digite um valor: '))
val3 = float(input('Digite um valor: '))


resultado = maior3(val1,val2,val3)

print(resultado)

# outra forma
#Função maior que 3 números
#float('inf')  float('-inf') 
def maior3(x,y=float('-inf'),z= float('-inf') ): 
  if x >= y and x >= z :
    return x
  elif y >=x and y >=z :
    return y
  else:
    return z


maior3(-30,-50)
