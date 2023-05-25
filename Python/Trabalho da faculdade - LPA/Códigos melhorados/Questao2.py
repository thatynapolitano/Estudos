#Criei uma função para imprimir o meu menu e evitar repetições no futuro 
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

codigo = int(input("Entre com o código desejado: "))

valorPedido = 0
#Função que atualiza o pedido 
def atualizaPedido(valorPedido, tipoProduto, valorProduto4302056): #Valor do produto com o meu RU
    valorAtualizado = valorPedido + valorProduto4302056
    print(f"Você pediu um {tipoProduto} no valor de {valorProduto4302056}") 
    return valorAtualizado 

while codigo:
    if codigo == 100:
        tipoProduto = "Cachorro Quente"
        valorProduto4302056 = 9
    elif codigo == 101:
        tipoProduto = "Cachorro Quente Duplo"
        valorProduto4302056 = 11
    elif codigo == 102:
        tipoProduto = "X-Egg"
        valorProduto4302056 = 12
    elif codigo == 103:
        tipoProduto = "X-Salada"
        valorProduto4302056 = 12
    elif codigo == 104:
        tipoProduto = "X-Bacon"
        valorProduto4302056 = 14
    elif codigo == 105:
        tipoProduto = "X-Tudo"
        valorProduto4302056 = 17
    elif codigo == 200:
        tipoProduto = "Refrigerante Lata"
        valorProduto4302056 = 5
    elif codigo == 201:
        tipoProduto = "Chá Gelado"
        valorProduto4302056 = 4
    else:
        print("Opção inválida")
        menu()
        codigo = int(input("Entre com o código desejado: "))
        continue
    
    valorPedido = atualizaPedido(valorPedido, tipoProduto, valorProduto4302056) #caso o cliente queira pedir mais alguma coisa e as condições
    print("Deseja pedir mais alguma coisa?")
    print("1- Sim")
    print("0- Não")
    resposta = int(input(""))
    if resposta == 1: 
        codigo = int(input("Entre com o código desejado: ")) 
        continue
    elif resposta == 0:
        print(f"O valor total é: {valorPedido}") 
        break