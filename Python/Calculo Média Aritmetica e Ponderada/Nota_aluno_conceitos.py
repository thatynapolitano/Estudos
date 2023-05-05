#Leia 3 notas de um aluno e imprima sua média.
# Caso esteja acima de 7 imprima "aprovado".
# Caso estreja entre 7 e 4 imprima "final".
# Caso esteja abaixo de 4 imprima "reprovado".

nota1 = float(input("Insira a sua primeira nota aqui:")) 
nota2 = float(input("Insira a sua segunda nota aqui:")) 
nota3 = float(input("Insira a sua terceira nota aqui:")) 

media = (nota1 + nota2 + nota3)/3
print("Sua média é:", media)

if media >= 7:
    print("Aprovado")
elif media >= 4 and media < 7:
    print("Final")
else: 
    print("Reprovado")
