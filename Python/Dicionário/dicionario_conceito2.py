


#Estrutura de um dicionário:
dic = {"nome":"Thati", "idade": 28, "altura": 1.66} # O "nome" é a chave e "Thati" é o valor
print(dic)

#Para acessar o valor de uma chave dentro de um dicionario 
print(dic["idade"])

#Adicionando elementos em um dicionário 

dic["programador"] = True 
print(dic)

#Subscrever um conteúdo. (Quando já existe uma chave, mas queremos mudar o valor dela)
dic["altura"] = 1.70
print(dic["altura"]) 

# Iterando sobre um dicionario 

# Para percorrer as chaves:
for chave in dic: 
    print(chave) 

# Para percorrer valor e chave: 

for chave in dic: 
    print(chave,dic[chave])

# Testando a existência de uma chave
print('peso' in dic) # O retorno será False
print('altura' in dic) # O retorno será True 
