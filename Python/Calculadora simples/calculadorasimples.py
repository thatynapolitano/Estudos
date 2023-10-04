def calculate(): 
    numero_1 = float(input("Digite um número: "))
    operador = input("Digite um operador (+,-,* ou /): ")
    numero_2 = float(input("Digite outro número: "))


    if operador == "+":
        print(f"{numero_1} + {numero_2} = ")
        print(numero_1 + numero_2 )
    elif operador == "-":
        print(f"{numero_1} - {numero_2} = ")
        print(numero_1 - numero_2 )
    elif operador == "*":
        print(f"{numero_1} * {numero_2} = ")
        print(numero_1 * numero_2 )
    elif operador == "/":
        print(f"{numero_1} / {numero_2} = ")
        print(numero_1 / numero_2 )
    else:
        print("Por favor, insira um operador válido.")

calculate()