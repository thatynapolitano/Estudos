lista=[0,9,2,2,3,3,2,7,8,3,0,3,7,1,9,4,2,7,8,9,3,2,6]

for i in range(10): #i =0 => 9
  cont=0
  for num in lista: #para cada número na lista
    if num == i:
      cont+=1
  print(f'{i} apareceu {cont} vezes')