palpite = int(input("Insira seu palpite aqui: "))
resposta = 10000

while palpite != resposta: 
    if palpite < resposta:
        print("Um pouco mais!")
    else: 
        print("Um pouco menos!")
    palpite = int(input("Insira uma resposta: "))
print("Acertou!")
    