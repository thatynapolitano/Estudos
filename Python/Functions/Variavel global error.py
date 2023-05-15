num=10

def func():
  global num # permite alteração de uma variável global no contexto geral
  num+=1
  print(num)

func()