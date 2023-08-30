# Iterar dicionários

# A forma mais comum para percorrer os dados de um dicionário é utilizando o comando for.

contatos = {
    "thatiana@gmail.com": {"nome":"Thatiana", "telefone": "1234-6789"},
    "andre@gmail.com": {"nome":"André", "telefone": "1234-6789"},
    "lucia@gmail.com": {"nome":"Lúcia", "telefone": "1234-6778"},
    "taiyang@gmail.com": {"nome":"Taiyang", "telefone": "1234-1234"},
}

for chave in contatos:
    print(chave,contatos[chave])

for chave, valor in contatos.items():
    print(chave,valor)