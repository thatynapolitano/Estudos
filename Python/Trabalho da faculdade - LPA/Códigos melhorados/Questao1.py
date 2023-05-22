print("Bem-Vindo(a) a Loja de Thatiana de Assis Napolitano (RU: 4302056)")

#Peço para que o usuário entre com o valor do produto e a quantidade do produto

valorProduto4302056 = float(input("Entre com o valor do produto: ")) #Variavel com RU
qtdProduto = int(input("Entre com a quantidade: "))
semDesconto = 0
desconto = 0

#Crio abaixo minhas condições com os respectivos cálculos de sem desconto e com desconto em cada situação pedida.

semDesconto = qtdProduto * valorProduto4302056
print("O valor da compra sem desconto foi: R$ {:.2f}".format(semDesconto))

if qtdProduto <= 9:  
        porcentagem = "0%"
        desconto = semDesconto 
elif qtdProduto <= 99:  
        porcentagem = "5%"
        desconto = semDesconto - (semDesconto * 0.05)  
elif qtdProduto <= 999: 
        porcentagem = "10%"
        desconto = semDesconto - (semDesconto * 0.10) 
else:  
        porcentagem = "15%"
        desconto = semDesconto - (semDesconto * 0.15) 

print("O valor da compra com desconto foi: R$ {:.2f} (Desconto de: {})".format(desconto, porcentagem))  
