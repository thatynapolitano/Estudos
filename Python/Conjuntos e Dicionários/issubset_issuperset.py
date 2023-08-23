# ().ISSUBSET 
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}


conjunto_a.issubset(conjunto_b) # Todos os valores do conjunto a estão em b? Retorna verdadeiro ou falso
conjunto_b.issubset(conjunto_a) # Todos os valores do conjunto b estão em a? Retorna verdadeiro ou falso
print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a) )

# ().ISSUPERSET 
# É a pergunta oposta de ISSUBSET

conjunto_a.issuperset(conjunto_b) # Todos os valores do conjunto b estão em a? Retorna verdadeiro ou falso
conjunto_b.issuperset(conjunto_a) # Todos os valores do conjunto a estão em b? Retorna verdadeiro ou falso
print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))

