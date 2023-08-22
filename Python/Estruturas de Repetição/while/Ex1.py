# contar e imprimir de 0 a 50 mas pular 30
indice = 0
while (indice <= 50):
  if(indice != 30):
    print(indice)
  indice = indice + 1

# incrementar contagem
# a partir do zero até contagem seja igual a 3721
# quando contagem for igual a 3721 sair do while e imprimir 'saiu !'

numero = 0
while (numero < 3200):
  numero += 1
  if (numero == 3000):
    continue
print('saiu ' , numero)