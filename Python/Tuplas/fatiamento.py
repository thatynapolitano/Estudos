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