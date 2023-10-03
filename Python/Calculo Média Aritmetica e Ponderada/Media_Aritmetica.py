#Leia tres notas de um aluno (0~10) e informe a media 

#ATALHO: CTRL + ALT + SETA PRA CIMA OU PRA BAIXO para duplicar o codigo nas linhas de cima ou de baixo <33333 

print('Informe suas 3 notas:')
nota1 = float(input('Digite sua nota 1:'))
nota2 = float(input('Digite sua nota 2:'))
nota3 = float(input('Digite sua nota 3:')) 

media = (nota1+nota2+nota3)/3 
print('O resultado eh:', media)  
print(f'O resultado eh: {media:.2f}') # Dessa forma eu defino quantas casas decimais eu quero que mostre o resultado. 


# Exercício:  Sua solução deverá realizar o cálculo da média aritmética simples tendo como entrada 4 notas e como saída o conceito: 

# Média acima de 70	Aprovado
# Média entre 40 e 70	Exame
# Média abaixo de 40	Reprovado

# Para o exame solicita-se uma nova nota e é feita a soma da média obtida no período regular + nota obtida no exame. O resultado da soma é dividido por 2 e se o resultado for igual ou superior à 50 será “Aprovado”, caso contrário, “Reprovado”.

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
    if recuperacao >= 5.0:
        print("Aprovado")
    else: 
        print("Reprovado")
else: 
    print("Reprovado")
