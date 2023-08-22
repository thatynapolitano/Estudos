# Faca um codigo que imprima os numeros de 1 ate 50 em ordem crescente e depois em ordem descrescente. Seu codigo deve pular o numero 37.

for i in range(1,51): # Vai do 1 ate o 51, sem contar o 51. logo 1-50
    if i != 37: # i diferente de 37
        print(i)

# Outra forma

for i in range(1,51):
    if i == 37: 
        continue # o comando continue ignora aquela iteracao, no caso o 37. E continua o loop.
    print(i)

# Para colocar em ordem decrescente

for i in range(50,0,-1): #Vai do 50 ate o 0, indo de -1 em -1 
    if i == 37: 
        continue
    print(i)

# Vamos supor que eu quisesse terminar o programa quando chegasse no número 37.  Break interrompe o loop.

for i in range(50,0,-1): #Vai do 50 ate o 0, indo de -1 em -1 
    if i == 37: 
        break
    print(i)

# Para dar espaco entre os numeros na mesma linha 

for i in range(50,0,-1): #Vai do 50 ate o 0, indo de -1 em -1 
    if i == 37: 
        break
    print(i, end = ' ') # end =   <- é padrão para imprimir um valor de determinada forma, no caso colocamos um espaço. 

