# Del

contatos = {
    "thatiana@gmail.com": {"nome":"Thatiana", "telefone": "1234-6789"},
    "andre@gmail.com": {"nome":"André", "telefone": "1234-6789"},
    "lucia@gmail.com": {"nome":"Lúcia", "telefone": "1234-6778"},
    "taiyang@gmail.com": {"nome":"Taiyang", "telefone": "1234-1234"},
}

#print(contatos)

del contatos ["thatiana@gmail.com"]["telefone"]
del contatos ["lucia@gmail.com"]

print(contatos)