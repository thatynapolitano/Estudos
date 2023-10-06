def media_aritmetica_simples():
    nota_1 = float(input("Digite a sua primeira nota aqui: ")) 
    nota_2 = float(input("Digite a sua segunda nota aqui: ")) 
    nota_3 = float(input("Digite a sua terceira nota aqui: ")) 
    nota_4 = float(input("Digite a sua quarta nota aqui: ")) 

    media_aritmetica = (nota_1 + nota_2 + nota_3 + nota_4) / 4 

    print(f"Média aritmética: {media_aritmetica}")

    if media_aritmetica >= 7.0: 
        print("Aprovado")
    elif media_aritmetica >= 4.0 and media_aritmetica <= 7.0: 
        print("Exame")
        nota_exame= float(input("Insira a nota do exame: "))
        recuperacao = (nota_exame + media_aritmetica) / 2
        print(recuperacao)
        if recuperacao >= 5.0:
            print("Aprovado")
        else: 
            print("Reprovado")
    else: 
        print("Reprovado") 


def ordenacao():
    numeros = []

    for numero in range(4):
        numero = int(input("Digite um número: "))
        for chave, valor in enumerate(numeros):
            if numero < valor:
                numeros.insert(chave, numero)
                break
        else:
            numeros.append(numero)
        print("Lista atual:", numeros)


def calculadora(): 
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


def calculadora_imc():
    altura = float(input("Digite a sua altura aqui: "))
    peso = float(input("Digite o seu peso aqui: "))


    IMC = peso / altura ** 2 
    print(f"O seu IMC é: {IMC:.2f}") 


    if IMC < 18.5: 
        print("Abaixo do peso")
    elif IMC >= 18.6 and IMC <= 24.9:
        print("Peso ideal (Parabéns!)")
    elif IMC >= 25 and IMC <= 29.9:
        print("Levemente acima do peso")
    elif IMC >= 30 and IMC <= 34.5:
        print("Obesidade Leve (grau I)")
    elif IMC >= 35 and IMC <= 39.9:
        print("Obesidade Severa (grau II)")
    else:
        print("Obesidade Mórbida (grau III)")


def sacar_dinheiro():
    
    valor_solicitado = int(input("Digite o valor a ser sacado: R$ "))
    notas_disponiveis = [100, 50, 20]
    resultado = {}
    valor_debitado = 0

    for nota in notas_disponiveis:
        quantidade_notas = valor_solicitado // nota
        if quantidade_notas > 0:
            resultado[f"R$ {nota}"] = quantidade_notas
            valor_debitado += quantidade_notas * nota
            valor_solicitado -= quantidade_notas * nota

    if valor_solicitado > 0:
        print("Não é possível entregar notas de R$ 5 ou outros valores. Valor residual não será debitado da conta.")

    print("Notas a serem entregues:")
    for nota, quantidade in resultado.items():
        print(f"{quantidade} nota(s) de {nota}")

    print(f"Total debitado da conta: R$ {valor_debitado}")


while True:
 try:
    opcao = int(input("Escolha a opção desejada: \n"
                   "1-Media aritmetica simples \n"
                   "2-Ordenação de 4 números \n"
                   "3-Calculadora de IMC \n"
                   "4-Calculadora \n"
                   "5- Máquina de saques automáticos \n"
                   "6-Sair\n>>"))
    if opcao == 1:
        media_aritmetica_simples()
    elif opcao == 2:
        ordenacao()
    elif opcao == 3:
        calculadora_imc()
    elif opcao == 4:
        calculadora()
    elif opcao == 5:
        sacar_dinheiro()
    elif opcao == 6:
        print("Programa finalizado")
        break 
    else:
        print("Digite uma opção válida")
        continue
 except ValueError:
    print("Digite uma opção válida. Digite valores inteiros para acessar a opção desejada.")