#Cria uma copia de um dicionario 

contatos = {
    "thatiana@gmail.com": {"nome":"Thatiana", "telefone":"3333-3333"}
}

copia = contatos.copy() 
copia ["thatiana@gmail.com"] = {"nome":"Thaty"}

contatos["thatiana@gmail.com"]
print(contatos["thatiana@gmail.com"])  

print(copia["thatiana@gmail.com"])

