# Quando eu quero concatenar uma lista com outra (adicionar valores de uma lista em outra)

linguagens = ["python", "js", "c"]

print(linguagens)

linguagens.extend(["java", "c#"])

print(linguagens)

#Outra forma de juntar uma lista com outra: 

lista1 = [1,2,3,4,5] 
lista2 = [6,7,8,9,10] 

lista1.extend(lista2)

print(lista1) 
