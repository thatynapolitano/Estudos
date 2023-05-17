#            0       1       2       3       4
alunos = ['Mario','Luigi','Yoshi','Peach','Toad']

# Contabilizar quantas letras "a" aparece na lista "alunos"

contador = 0
for alunos in alunos:
    for letra in alunos:
        if letra == "a":
            contador+=1

print(contador)
