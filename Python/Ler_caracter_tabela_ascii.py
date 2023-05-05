#Leia um caracter, o que é? 
#Uma letra, um número ou um símbolo 
# a função ord é de acordo com a tabela ascii. quero identificar se é um numero, simbolo ou letra. 

caracter=ord(input("Digite um caracter: "))

if caracter >= 48 and caracter <= 57:
    print("É um número")
elif caracter >= 58 and caracter <= 64:
    print("É um símbolo")
else:
    print("É uma letra")





