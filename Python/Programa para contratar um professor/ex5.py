# Programa para contratar um professor. 
# Critério 1: experiencia em sala de aula >= 60 meses
# Critério 2: E publicações nos últimos 2 anos >= 3 
 
Experiencia=int(input('Quantos meses tem de experiência em sala de aula?'))
Publicacoes=int(input('Quantas publicacoes tem nos últimos 2 anos?'))

if Experiencia >= 60 and Publicacoes >= 3: 
    print('Atende')
else:
    print('Não atende')