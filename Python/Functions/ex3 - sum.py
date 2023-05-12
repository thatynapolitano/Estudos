def soma3(x,y,z):  # Se o usuário não passar o parametro x, o valor de x será 0. E assim sera com os outros parametros y e z, caso o usuario não declare o parametro.
  soma = x+y+z
  print(soma) 

soma3(10,20,30)

# Ex:
def soma3(x=0,y=0,z=0): #parametro opcional
  soma = x+y+z
  multiplicacao= x*y*z
  return soma #retorna o valor para quem chamou a função, retorna apenas soma... a multiplicacao existe apenas dentro da função
  
resposta = soma3(10,20,30) + soma3(40,50,60)
resposta+=1
print(resposta)
