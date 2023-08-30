# setdefault 

# Se o atributo nao estiver no dicionario, ele adiciona com um valor que coloco como parametro. 

contato = {"nome": "Thatiana", "telefone": "3333-3333"}

contato.setdefault("nome", "Giovana") 
print(contato)  # Se não existe essa chave com esse atributo, ele nao vai retornar nada. Apenas as keys e os valores do dicionario.

contato.setdefault("idade",28) # aqui então passo o nome da chave e seu respectivo valor que quero adicionar no meu dicionario.
print(contato) 