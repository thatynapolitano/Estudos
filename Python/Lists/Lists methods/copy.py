# O copy vai retornar uma lista igual, mas com uma instancia diferente. Ou seja, não retorna a mesma lista.

lista = [1, "Python", [40,30,20]]

l2 = lista.copy()

print(lista)
print(l2) 

print(id(lista), id(l2))

# Ao analisarmos os IDs das listas, percebemos que possuem IDs diferentes, ou seja, são listas diferentes, mesmo que tenham os mesmos valores, não compartilham do mesmo ID.
# Sendo assim podemos criar copias de uma lista, fazer alterações nela, sem alterar a lista original. 

