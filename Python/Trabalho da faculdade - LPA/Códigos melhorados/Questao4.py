print("Controle de Estoque - Bicicletaria Thatiana de Assis Napolitano (RU: 4302056)")

listaPecas = []

def cadastrarPeca(codigo): # Função para cadastrar a peça que estará em um dicionário 
    print("Você selecionou a Opção de Cadastrar Peça")
    print("Código da peça é: 00{}".format(codigo))
    nome = input("Por favor entre com o NOME da peça: ")
    fabricante = input("Por favor entre com o FABRICANTE da peça: ")
    valor = float(input("Por favor entre com o VALOR (R$) da peça: "))
    dicionarioPeca = {  "codigo" : codigo,
                        "nome" : nome,
                        "fabricante" : fabricante,
                        "valor" : f'{valor:.2f}' }
    listaPecas.append(dicionarioPeca.copy()) # Adiciono as infos da peça na minha lista. Crio uma cópia do dicionário para que não ocorra a possibilidade de perder informações anteriores colocando novas inforrmações de peça.

def consultarPeca():
 while True:
    try:
     print("Você selecionou a Opção de Consultar Peças")   
     consultar = int(input("Entre com a opção desejada: \n"
                   "1-Consultar Todas as Peças \n"
                   "2-Consultar Peças por Código \n"
                   "3-Consultar Peças por Fabricante \n"
                   "4-Retornar\n>>"))
     if consultar == 1:
        print("-"*20)
        for peca in listaPecas: # selecionar cada dicionario da minha lista (cada peça da listaPeças)
         for key, value in peca.items(): # selecionar cada conjunto chave/valor do dicionario.(ex: "nome" : pedivela)
            print("{} : {}" .format(key,value))
        print("-"*20)
     elif consultar == 2:
        print("-"*20)
        entrada = int(input("Digite o código desejado: "))
        for peca in listaPecas:
           if (peca["codigo"] == entrada):
            for key, value in peca.items():
               print("{} : {}" .format(key,value))
        print("-"*20)
     elif consultar == 3:
        print("-"*20)
        entrada = input("Digite o fabricante desejado: ")
        for peca in listaPecas:
           if (peca["fabricante"] == entrada):
            for key, value in peca.items():
               print("{} : {}" .format(key,value))
        print("-"*20)
     elif consultar == 4:
        break 
     else:
        print("Digite uma opção válida")
        continue
    except ValueError:
       print("Digite uma opção válida. Digite valores inteiros para acessar a opção desejada.")


def removerPeca(): # Função para remover a peça a partir do código 
    print("Você selecionou a Opção de Remover Peça")
    entrada = int(input("Digite o código da peça a ser removida: "))
    for peca in listaPecas:
      if (peca["codigo"] == entrada):   
       listaPecas.remove(peca)
    print("Peça removida.")

print("Bem-vindo(a) ao Controle de Estoque da Bicicletaria de Thatiana de Assis Napolitano (RU:4302056)")

codigo4302056 = 0 #Variavel com o meu RU 

while True:
 try:
    opcao = int(input("Escolha a opção desejada: \n"
                   "1-Cadastrar Peças \n"
                   "2-Consultar Peças \n"
                   "3-Remover Peças \n"
                   "4-Sair\n>>"))
    if opcao == 1:
        codigo4302056 += 1
        cadastrarPeca(codigo4302056)
    elif opcao == 2:
        consultarPeca()
    elif opcao == 3:
        removerPeca()
    elif opcao == 4:
        print("Programa finalizado")
        break 
    else:
        print("Digite uma opção válida")
        continue
 except ValueError:
    print("Digite uma opção válida. Digite valores inteiros para acessar a opção desejada.")



