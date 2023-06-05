# Pergunte para um usuário sua ID e senha. Caso a ID seja 223344 e a senha 556677 imprima "acesso liberado". Caso contrario, imprima a mensagem: "Desculpa usuario #<ID>, ID/senha não conferem"


ID = int(input("ID:")) 
senha = int(input("Senha:"))

if ID == 223344 and senha == 556677: 
    print("Acesso liberado")
else:
    print("Acesso negado. \n ID ou senha incorreta.")