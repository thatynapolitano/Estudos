# Dicionários são conjuntos, mas neles sempre terão uma chave acompanhada de um valor. (Key e value) 

""" EXEMPLO:
Quero cadastrar um jogo. O jogoNome, jogoDesenvolvedora, jogoAno, etc. Quanto mais informações sobre o mesmo item (JOGO) mais desorganizado fica.
Ao invés de criar várias variáveis, eu posso criar um dicionário com as chaves e seus valores como no exemplo abaixo:
"""

jogo = {"Nome": "Super Mario", 
        "Desenvolvedora": "Nintendo",
        "Ano": 1990 }

print(jogo["Nome"]) #Aqui posso acessar a chave específica do Nome do Jogo.
print(jogo)

#E se eu quiser adicionar mais 1 chave com valor ao meu jogo. No caso a chave "gênero" com valor "aventura". 

jogo["Genero"] = "Aventura"
print(jogo)

#Se quiser atualizar chaves e valores já existentes 
jogo.update({"Ano": 1991, "Genero":"Plataforma"})
print(jogo)

#Retorna apenas as chaves: 
jogo.keys()
#Retorna apenas os valores:
jogo.values()
#Devolve uma lista com tuplas (chave, valor)
jogo.items() 

