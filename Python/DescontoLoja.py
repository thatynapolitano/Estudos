def menu():
    print("Bem-Vindo(a) a Lanchonete da Thatiana de Assis Napolitano (RU:4302056)")
    print(15*"*" + "Cardarpio" + 15*"*")
    print("| " +  "Codigo" + " |" + "       " + "Descricao" + "       " + "| " +  "Valor"  + " |")
    print("|  "  +  "100" + "   |" + "   " + "Cachorro Quente" +"     " + "|  " +  "9,00"  + " |")
    print("|  "  +  "101" + "   |" + " " + "Cachorro Quente Duplo" +" " + "| " +  "11,00"  + " |")
    print("|  "  +  "102" + "   |" + "        " + "X-Egg" + "          " + "| " + "12,00"  + " |")
    print("|  "  +  "103" + "   |" + "     " + "X-Salada" + "          " + "| " + "12,00"  + " |")
    print("|  "  +  "104" + "   |" + "      " + "X-Bacon" + "          " + "| " + "14,00"  + " |")
    print("|  "  +  "105" + "   |" + "      " + "X-Tudo" + "           " + "| " + "17,00"  + " |")
    print("|  "  +  "200" + "   |" + "   " + "Refrigerante Lata" + "   " + "|  " +  "5,00"  +  " |")
    print("|  "  +  "201" + "   |" + "      " + "Cha Gelado" + "       " + "|  " +  "4,00"  +  " |")

menu()

lista = [100, 101, 102, 103, 104, 105, 200, 201]

codigo = int(input("Entre com o código desejado: "))

while codigo not in lista:
    print("Opção inválida")
    menu()
    codigo = int(input("Entre com o código desejado: "))

acumulador = 0

while codigo in lista:
    if codigo == 100:
        acumulador = acumulador + 9
        print("Você pediu um Cachorro-Quente no valor de 9,00 reais")
        print("Deseja pedir mais alguma coisa?")
        print("1- Sim")
        print("0- Não")
        resposta=int(input(""))
        if resposta == 1: 
            codigo = int(input("Entre com o código desejado: ")) 
            continue
        elif resposta == 0:
            print(f"O valor total é: {acumulador}") 
            break
    elif codigo == 101:
        acumulador = acumulador + 11
        print("Você pediu um Cachorro Quente Duplo no valor de 11,00 reais")
        print("Deseja pedir mais alguma coisa?")
        print("1- Sim")
        print("0- Não")
        resposta=int(input("")) 
        if resposta == 1: 
            codigo = int(input("Entre com o código desejado: ")) 
            continue
        elif resposta == 0:
            print(f"O valor total é: {acumulador}") 
            break
    elif codigo == 102:
        acumulador = acumulador + 12
        print("Você pediu um X-Egg o no valor de 12,00 reais")
        print("Deseja pedir mais alguma coisa?")
        print("1- Sim")
        print("0- Não")
        resposta=int(input(""))
        if resposta == 1: 
            codigo = int(input("Entre com o código desejado: ")) 
            continue
        elif resposta == 0:
            print(f"O valor total é: {acumulador}") 
            break
    elif codigo == 103:
        acumulador = acumulador + 12
        print("Você pediu uma X-Salada no valor de 12,00 reais")
        print("Deseja pedir mais alguma coisa?")
        print("1- Sim")
        print("0- Não")
        resposta=int(input(""))
        if resposta == 1: 
            codigo = int(input("Entre com o código desejado: ")) 
            continue
        elif resposta == 0:
            print(f"O valor total é: {acumulador}") 
            break
    elif codigo == 104:
        acumulador = acumulador + 14
        print("Você pediu um X-Bacon no valor de 14,00 reais")
        print("Deseja pedir mais alguma coisa?")
        print("1- Sim")
        print("0- Não")
        resposta=int(input(""))
        if resposta == 1: 
            codigo = int(input("Entre com o código desejado: ")) 
            continue
        elif resposta == 0:
            print(f"O valor total é: {acumulador}") 
            break
    elif codigo == 105:
        acumulador = acumulador + 17
        print("Você pediu um X-Tudo no valor de 17,00 reais")
        print("Deseja pedir mais alguma coisa?")
        print("1- Sim")
        print("0- Não")
        resposta=int(input(""))
        if resposta == 1: 
            codigo = int(input("Entre com o código desejado: ")) 
            continue
        elif resposta == 0:
            print(f"O valor total é: {acumulador}") 
            break
    elif codigo == 200:
        acumulador = acumulador + 5
        print("Você pediu um Refrigerante Lata no valor de 5,00 reais")
        print("Deseja pedir mais alguma coisa?")
        print("1- Sim")
        print("0- Não")
        resposta=int(input(""))
        if resposta == 1: 
            codigo = int(input("Entre com o código desejado: ")) 
            continue
        elif resposta == 0:
            print(f"O valor total é: {acumulador}") 
            break
    elif codigo == 201:
        acumulador = acumulador + 4
        print("Você pediu um Chá Gelado no valor de 4,00 reais")
        print("Deseja pedir mais alguma coisa?")
        print("1- Sim")
        print("0- Não")
        resposta=int(input(""))
        if resposta == 1: 
            codigo = int(input("Entre com o código desejado: ")) 
            continue
        elif resposta == 0:
            print(f"O valor total é: {acumulador}") 
            break







    

