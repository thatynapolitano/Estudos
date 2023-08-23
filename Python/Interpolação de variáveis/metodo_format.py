# Interpolação de variáveis em Método format

nome = "Thatiana"
idade = 28
profissao = "Programadora e Analista de Dados"
linguagem = "Python"

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao,linguagem))

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.".format(nome, idade, profissao,linguagem))


#f - string
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

# Formatar Strings com f-string 
PI = 3.14159

print(f"Valor de PI: {PI: .2f}")
print (f"Valor de PI: {PI:10.2f}")
