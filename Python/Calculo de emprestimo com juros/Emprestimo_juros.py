# Assuma que uma pessoa efetuou um emprestimo, e que a multa por dia de atraso do emprestimo é de 2%. Pergunte ao usuario o total emprestado, o total de dias e informe o valor final que deve ser pago. Utilize juros simples. 

emprestimo = float(input('Digite o valor emprestado: '))
dias = int(input('Digite o valor de dias de atraso: '))
multa = emprestimo*0.02
total = emprestimo + (dias * multa)
print(f"O valor final a ser pago considerando os juros é de: R$ {total}")


# Modifique o programa para aceitar outras taxas de juros