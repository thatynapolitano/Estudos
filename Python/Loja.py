print("Bem-Vindo(a) a Loja de Thatiana de Assis Napolitano (RU: 4302056)")

valorProduto = float(input("Entre com o valor do produto: "))
qtdProduto = int(input("Entre com a quantidade: "))
semDesconto = 0
desconto = 0

if qtdProduto <= 9: #Se a quantidade do produto for menor ou igual a 9. 
    semDesconto = qtdProduto * valorProduto #Valor sem desconto
    print(f"O valor da compra é: R$ {semDesconto}")  #Não terá desconto 
elif qtdProduto <= 99: #Se a quantidade do produto for maior ou igual a 10 e menor igual a 99. 
    semDesconto = qtdProduto * valorProduto # Valor sem desconto 
    desconto = semDesconto - (semDesconto * 0.05) # Calcular o desconto de 5%
    print("O valor da compra sem desconto foi: R$ {:.2f}" .format(semDesconto))
    print("O valor da compra com desconto foi: R$ {:.2f} (Desconto de: 5%)" .format(desconto))  
elif qtdProduto <= 999: #Se a quantidade do produto for maior ou igual a 100 e menor igual a 999.
    semDesconto = qtdProduto * valorProduto # Valor sem desconto 
    desconto = semDesconto - (semDesconto * 0.10) # Calcular o desconto de 10%
    print("O valor da compra sem desconto foi: R$ {:.2f}" .format(semDesconto))
    print("O valor da compra com desconto foi: R$ {:.2f} (Desconto de: 10%)" .format(desconto))  
else:  #Se a quantidade do produto for maior do que as condições anteriores
    semDesconto = qtdProduto * valorProduto # Valor sem desconto 
    desconto = semDesconto - (semDesconto * 0.15) # Calcular o desconto de 15%
    print("O valor da compra sem desconto foi: R$ {:.2f}" .format(semDesconto))
    print("O valor da compra com desconto foi: R$ {:.2f} (Desconto de: 15%)" .format(desconto))

