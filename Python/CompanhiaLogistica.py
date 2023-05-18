print("Bem-vindo(a) a Companhia de Logística Thatiana de Assis Napolitano S.A (RU:4302056)")

def dimensoesObjeto():
    while True:  
        try: 
            comprimento = float(input("Digite a comprimento do objeto em cm: "))
            largura = float(input("Digite o largura do objeto em cm: "))
            altura = float(input("Digite a altura do objeto em cm: "))
            volume = altura * comprimento * largura
            print(f"O volume do objeto em cm³ é: {volume}")
            if volume <= 1000:
                return 10, volume
            elif volume >= 1001 and volume <= 10000:
                return 20, volume
            elif volume >= 10001 and volume <= 30000:
                return 30, volume
            elif volume >= 30001 and volume <= 100000:
                return 50, volume
            else:
                print("Não aceitamos objetos com dimensões tão grandes")
                print("Entre com as dimensões desejadas novamente")
        except ValueError: 
            print("O valor precisa ser numérico")
            print("Por favor entre com as dimensões desejadas novamente")

def pesoObjeto():
     while True:
        try: 
            peso = float(input("Digite o peso do objeto em kg: "))
            print(f"O peso do objeto em kg é: {peso}")
            if peso <= 0.1:
                return 1
            elif peso >= 0.11 and peso <= 1:
                return 1.5
            elif peso >= 1.10 and peso <= 10:
                return 2
            elif peso >= 10.1 and peso <= 30:
                return 3
            else: 
                print("Não aceitamos objetos tão pesados")
                print("Por favor entre com as dimensões desejadas novamente")
        except ValueError: 
            print("O valor precisa ser numérico")
            print(" Por favor entre com as dimensões desejadas novamente")

def rotaObjeto(): 
    print("Selecione a rota:")
    print("BR - De Brasília para Rio de Janeiro")
    print("BS - De Brasília para São Paulo")
    print("RB - De Rio de Janeiro para Brasília")
    print("RS - De Rio de Janeiro para São Paulo")
    print("SR - De São Paulo para Rio de Janeiro")
    print("SB - De São Paulo para Brasília")
    while True:
        rotas = {
            "RS": 1,
            "SR": 1,
            "BS": 1.2,
            "SB": 1.2,
            "BR": 1.5,
            "RB": 1.5
        }
        rota = input("")
        if rota in rotas:
            return rotas[rota]
        else:
            print("Você digitou uma rota que não existe.")
            print("Por favor entre com a rota desejada novamente")
        

# Formas de chamar as funções para compor a fórmula de cacular o total a ser pago 
dimensoes,volume = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()

total = dimensoes * peso * rota
print("Valor total a ser pago: R$", total)
