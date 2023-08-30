# Pop - Remove uma chave do dicionario

contatos = {
    "thatiana@gmail.com": {"nome":"Thatiana", "telefone":"3333-3333"}
}

resultado = contatos.pop("thatiana@gmail.com")
print(resultado) 

resultado = contatos.pop("thatiana@gmail.com", "não encontrou")
print(resultado)

