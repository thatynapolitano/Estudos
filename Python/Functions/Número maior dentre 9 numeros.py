#Função maior que 9 números
def maior3(x,y,z):
  if x >= y and x >= z :
    return x
  elif y >=x and y >=z :
    return y
  else:
    return z

m1 = maior3(10,20,30)

m2 = maior3(40,50,60)

m3 = maior3(70,80,90)

resultado = maior3(m1,m2,m3)

print(resultado)

# Outra forma 

#Função maior que 9 números
def maior3(x,y,z):
  if x >= y and x >= z :
    return x
  elif y >=x and y >=z :
    return y
  else:
    return z

v1 = input('digite valor: ')
v2 = input('digite valor: ')
v3 = input('digite valor: ')
v4 = input('digite valor: ')
v5 = input('digite valor: ')
v6 = input('digite valor: ')
v7 = input('digite valor: ')
v8 = input('digite valor: ')
v9 = input('digite valor: ')


m1 = maior3(v1,v2,v3)

m2 = maior3(v4,v5,v6)

m3 = maior3(v7,v8,v9)

resultado = maior3(m1,m2,m3)

print(resultado)