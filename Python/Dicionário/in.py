# IN
#Para saber se existe uma chave ou não no nosso dicionario
# Retorna verdadeiro ou falso

contatos = {
    "thatiana@gmail.com": {"nome":"Thatiana", "telefone": "1234-6789"},
    "andre@gmail.com": {"nome":"André", "telefone": "1234-6789"},
    "lucia@gmail.com": {"nome":"Lúcia", "telefone": "1234-6778"},
    "taiyang@gmail.com": {"nome":"Taiyang", "telefone": "1234-1234"},
}


print("thatiana@gmail.com" in contatos)
print("adalberto@gmail.com" in contatos)
print("idade" in contatos ["taiyang@gmail.com"])
print("telefone" in contatos ["lucia@gmail.com"])
