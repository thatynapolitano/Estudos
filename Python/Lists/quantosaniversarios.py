#Exercício 5- Crie uma lista de 10 posições para simular 10 pessoas. Preencha cada posição da lista arbitrariamente com números entre 1 e 12 para indicar o mês de aniversário. Indique quantas pessoas fizeram aniversário em cada mês

listaMes = [3,9,12,4,8,9,3,2,11,2,11]

for mes in range(1,12):
    contador=0
for aniversario in listaMes:
  if aniversario == mes:
    contador+=1
print(f'No mês {mes} tivemos {contador} aniversários. ')

