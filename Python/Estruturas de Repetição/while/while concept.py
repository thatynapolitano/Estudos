#Comando while
# O comando while é usadoo para repetir um bloco de código várias vezes. Faz sentido usar while quando não sabemos o número exato de vezes que nosso bloco de código deve ser executado.


mao = 0 
while mao < 5: 
    print("Bom dia")
    mao += 1 # mão = mão + 1  <- O incremento tem que ocorrer para que o meu loop não seja eterno. 

    
mao = 0 
while mao < 5: 
    print("Bom dia" , mao)  # Para adicionar um contador 
    mao += 1

opcao = -1 

while opcao != 0:
    opcao = int(input("[1] Sacar \n [2] Extrato \n [0] Sair /n:  "))

    if opcao ==1:
        print("Sacando...")
    elif opcao ==2:
        print("Exibindo o extrato...")

        