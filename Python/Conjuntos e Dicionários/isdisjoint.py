# ().ISDISJOINT   (O conjunto X tem intersecção com o conjunto Y?) Retorna verdadeiro ou falso. 

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1,0}

conjunto_a.isdisjoint(conjunto_b) # True
conjunto_a.isdisjoint(conjunto_c) # False

print(conjunto_a.isdisjoint(conjunto_b)) # True
print(conjunto_a.isdisjoint(conjunto_c)) # False