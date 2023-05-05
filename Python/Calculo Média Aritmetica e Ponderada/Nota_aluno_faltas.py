# Modifique o exercicio anterior para aceitar a quantidade de faltas.

# 8 ou mais faltas imprima "reprovado por falta" e não imprima a média do aluno.


nota1 = float(input("Insira a sua primeira nota aqui:")) 
nota2 = float(input("Insira a sua segunda nota aqui:")) 
nota3 = float(input("Insira a sua terceira nota aqui:")) 
faltas = int(input("Digite suas faltas: "))

media = (nota1 + nota2 + nota3)/3
print("Sua média é:", media)

if faltas >= 8:
    print("Reprovado por faltas")
elif media >= 7:
    print("Aprovado")
elif media >= 4 and media < 7:
    print("Final")
else: 
    print("Reprovado")