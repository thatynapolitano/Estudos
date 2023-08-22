#Operadores de identidade 
curso = "Curso de Python"
nome_do_curso = curso 
saldo, limite = 200,200

pergunta = curso is nome_do_curso 
print(pergunta)

pergunta = curso is not nome_do_curso 
print(pergunta)

pergunta = saldo is limite 
print(pergunta)