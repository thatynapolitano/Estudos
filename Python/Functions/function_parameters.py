def saudacao (nome,curso):
  print(f"Seja bem-vindo, {nome}!")
  print(f"É um prazer ter você como parte do curso de {curso}") 

saudacao("André", "Python")

# Caso o curso por default seja Python, não é uma variável que você queira mudar quando a função for chamada, então você pode já definí-la como default da seguinte forma:

def saudacao (nome,curso="Python"):
  print(f"Seja bem-vindo, {nome}!")
  print(f"É um prazer ter você como parte do curso de {curso}") 

saudacao("André")  # Sendo assim eu não preciso passar mais o segundo parametro curso, apenas o nome. 

# Se você não passar o parametro de curso, por padrão o valor de curso será "Python". Porém, se vc chamar a função e passar um parametro curso diferente, esse irá aparecer na tela.

saudacao("André","C#") 



