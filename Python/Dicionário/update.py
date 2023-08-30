# Update para atualizar valores de chaves que já existem na minha lista

contatos = {
    "thatiana@gmail.com": {"nome":"Thatiana", "telefone":"3333-3333"}
} 

contatos.update({"thatiana@gmail.com" : {"nome":"Thaty"}})
print(contatos) 