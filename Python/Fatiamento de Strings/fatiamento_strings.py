#Fatiamento
s1 = 'Super Mario'
print(s1[0:5])#indice do 0 até 4
print(s1[:5]) #indice do 0 até 4
print(s1[6:11]) #indices de 6 até 10
print(s1[6:])
print(s1[0:-1])
print(s1[:-1]) #indice negativo
print(s1[:-2]) #indice negativo

#Fatiamento em passos
s1 = 'Super Mario'

print (s1[0:11:3]) #0-10 pulando de 3 em 3
print (s1[::2]) # inicio ao fim pulando de 2 em 2

#Outro exemplo de fatiamento 

nome = "Thatiana Napolitano"

nome[0]
print(nome[0]) 

nome[:8]
print(nome[:8])

nome[9:]
print(nome[9:])

nome[10:18]
print(nome[10:18])


nome[10:18:2]   # o terceiro valor é o step. 
print(nome[10:18:2])

nome[:]
print(nome[:])
