# FOR
# O comando FOR é usado para percorrer um objeto iterável. Faz sentido usar quando sabemos o número exato de vezes que nosso bloco de código deve ser executado, ou quando queremos percorrer um objeto iterável.

listaAlunos = ["mario", "luigi", "peach", "yoshi"]
for aluno in listaAlunos: 
    print("Bem vindo", aluno)

# printar numero de 1 a 10 
for i in range(1,11): # se eu colocar 10 no lugar do 11, a contagem vai até o número 9. Para garantir que vai até o valor final que no caso é o 10, preciso adicionar mais 1, assim fica 11.
    print(i)
    
for i in range(10, 0, -1):
    print(i)

# Outro exemplo:
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto: 
    if letra.upper() in VOGAIS:
        print(letra, end="")
print()