# Dicionários 

# Um dicionário é um conjunto não-ordenado de pares chave:valor,  onde as chaves são únicas em uma dada instância do dicionário. Dicionários são delimitados por chaves: {}, e contém uma lista de pares chaves: valor separada por vírgulas.

# Existem duas formas de sintaxe de um dicionário
pessoa = {"nome": "Thatiana", "idade": 28}

pessoa = dict(nome="André", idade=23) 

pessoa ["telefone"] = "3333-1234" 

print(pessoa)

# Dicionários podem armazenar qualquer tipo de objeto Python como valor, desde que a chave para esse valor seja um objeto imutável como (strings e números). 

# Exemplo: 

contatos = {
    "thatiana@gmail.com": {"nome":"Thatiana", "telefone": "1234-6789"},
    "andre@gmail.com": {"nome":"André", "telefone": "1234-6789"},
    "lucia@gmail.com": {"nome":"Lúcia", "telefone": "1234-6778"},
    "taiyang@gmail.com": {"nome":"Taiyang", "telefone": "1234-1234"},
}

telefone = contatos["andre@gmail.com"]["telefone"]
print(telefone)

print(contatos["andre@gmail.com"]["telefone"])