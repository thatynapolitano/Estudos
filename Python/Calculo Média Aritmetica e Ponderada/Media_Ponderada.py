
# Agora calcule a media ponderada considerando os pesos: 1, 3 e 5 
# cada nota multiplica pelo seu peso e no final divide o resultado pela soma dos pesos 

print('Informe suas 3 notas:')
nota1 = float(input('Digite sua nota 1:'))
nota2 = float(input('Digite sua nota 2:'))
nota3 = float(input('Digite sua nota 3:')) 

media= (nota1*1 + nota2*3 + nota3*5) / 9 
print(f'Sua média é: {media:.2f}')



