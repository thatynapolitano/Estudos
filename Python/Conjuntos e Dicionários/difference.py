# ().DIFFERENCE 

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.difference(conjunto_b) 
conjunto_b.difference(conjunto_a) 

print(conjunto_a.difference(conjunto_b)) 
print(conjunto_b.difference(conjunto_a)) 

# ().SYMMETRIC_DIFFERENCE 
# Me retorna todos os valores diferentes dos conjuntos de uma vez só em um único conjunto. 

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4} 

conjunto_a.symmetric_difference(conjunto_b) 
print(conjunto_a.symmetric_difference(conjunto_b) )