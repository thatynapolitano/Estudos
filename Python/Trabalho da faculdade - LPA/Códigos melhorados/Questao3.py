print("Bem-vindo(a) a Companhia de Logística Thatiana de Assis Napolitano S.A (RU:4302056)")

def dimensoesObjeto(): # Função para calcular o volume do objeto, suas condições e captura de erro
    while True:  
        try: 
            comprimento = float(input("Digite a comprimento do objeto em cm: "))
            largura = float(input("Digite o largura do objeto em cm: "))
            altura = float(input("Digite a altura do objeto em cm: "))
            volume = altura * comprimento * largura
            print(f"O volume do objeto em cm³ é: {volume}")
            if volume < 1000:
                return 10, volume
            elif 1000 <= volume < 10000:
                return 20, volume
            elif 10000 <= volume < 30000:
                return 30, volume
            elif 30000 <= volume < 100000:
                return 50, volume
            else:
                print("Não aceitamos objetos com dimensões tão grandes")
                print("Entre com as dimensões desejadas novamente")
        except ValueError: 
            print("Você digitou alguma dimensão do objeto com valor não numérico")
            print("Por favor entre com as dimensões desejadas novamente")

def pesoObjeto(): # Função para calcular o peso do objeto e captura de erro 
     while True:
        try: 
            peso = float(input("Digite o peso do objeto em kg: "))
            print(f"O peso do objeto em kg é: {peso}")
            if peso <= 0.1:
                return 1
            elif 0.1 <= peso < 1:
                return 1.5
            elif 1 <= peso < 10:
                return 2
            elif 10 <= peso < 30:
                return 3
            else: 
                print("Não aceitamos objetos tão pesados")
                print("Por favor entre com as dimensões desejadas novamente")
        except ValueError: 
            print("Você digitou peso do objeto com valor não numérico")
            print("Por favor entre com as dimensões desejadas novamente")

def rotaObjeto(): # Função para definir a rota do objeto 
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
            return rotas[rota] #Retorno a rota escolhida pelo usuário. As rotas ficam armazenadas em dicionário.
        else:
            print("Você digitou uma rota que não existe.")
            print("Por favor entre com a rota desejada novamente")
        

# Chamo as funções para compor a fórmula de cacular o total a ser pago 
dimensoes,volume = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()

valorTotal4302056 = dimensoes * peso * rota # Variavel com o meu RU 
print("Valor total a ser pago: R$", valorTotal4302056)