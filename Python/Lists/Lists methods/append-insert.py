#Adicionando elementos a uma lista: append() e insert()

#Um novo elemento pode ser colado ao final da lista atual, utilizando o método append() e insert()
#Estrutura: lista.append(value)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista.append(10)  
print(lista)

#O método insert() é mais inteligente - ele pode adicionar um novo elemento em qualquer lugar na lista, não apenas no final.
#Estrutura:  lista.insert(location, value)

lista.insert(2, 20)
print(lista)

