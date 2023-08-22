# Operador E 
# Nesse caso todas as condições precisam ser verdadeiras. Caso uma delas seja falsa, o output será false.


saldo = 1000 
saque = 200
limite = 100 

pergunta = saldo >= saque and saque <= limite
print(pergunta)

# Operador Ou 
# Nesse caso um OU outro precisa ser verdadeiro para que o output seja verdadeiro. O output só será falso se ambos forem falsos.

saldo = 1000 
saque = 200
limite = 100 

pergunta = saldo >= saque or saque <= limite
print(pergunta)

#Operador de Negação 

pergunta = not 1000 > 1500
print(pergunta)

contatos_emergencia=[] #lista vazia é considerado falso
pergunta = not contatos_emergencia # então aqui fica True, por causa do not anteriormente.
print(pergunta)

pergunta = not "saque 1500;"
print(pergunta)

pergunta = not "" 
print(pergunta) 

# Parenteses para delimitar a precedencia de comparação
saldo = 1000 
saque = 200
limite = 100 
conta_especial = True

pergunta = saldo <= saque and saque <= limite or conta_especial and saldo >= saque 
print(pergunta)

pergunta = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(pergunta)


