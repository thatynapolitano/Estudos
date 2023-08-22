
inicial = int (input('Digite onde deseja começar: ')) #inicial 5
final = int (input('Digite onde deseja finalizar: ')) #final 15

i=inicial #iteração -> cada execução, quantidades de execuções   
while i<=final:
  print('valor:',i)
  i+=1 # i= i+1

print('fim do código')



#somar valores em um intervalo
inicial = int (input('Digite onde deseja começar: ')) #inicial 5
final = int (input('Digite onde deseja finalizar: ')) #final 15

i=inicial 
soma=0
while i<=final:
  print('valor:',i)
  soma= soma+i
  i+=1 # i= i+1

print('valor acumulado',soma)