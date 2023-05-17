#Listas
#Diferentemente das tuplas, podemos sim modificar as listas. No exemplo abaixo eu substituí Mario (na posição 0) por Super Mario! :)

#          0          1         2       3        4 
alunos = ["Mario", "Luigi", "Yoshi", "Peach", "Toad"]
alunos[0] = "Super Mario"
print(alunos)

# Remover algum elemento da lista  - Para remover pela posição do elemento 
del alunos[1]
print(alunos)

# Outra forma de remover - Para remover pelo conteúdo 
alunos.remove("Yoshi")

alunos.insert(2, "Bowser")
alunos.append("Wario")
print(alunos)

