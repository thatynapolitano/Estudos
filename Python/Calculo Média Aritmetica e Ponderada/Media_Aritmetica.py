#Leia tres notas de um aluno (0~10) e informe a media 

#ATALHO: CTRL + ALT + SETA PRA CIMA OU PRA BAIXO para duplicar o codigo nas linhas de cima ou de baixo <33333 

print('Informe suas 3 notas:')
nota1 = float(input('Digite sua nota 1:'))
nota2 = float(input('Digite sua nota 2:'))
nota3 = float(input('Digite sua nota 3:')) 

media = (nota1+nota2+nota3)/3 
print('O resultado eh:', media)  
print(f'O resultado eh: {media:.2f}') # Dessa forma eu defino quantos casas decimais eu quero que mostre o resultado. 
