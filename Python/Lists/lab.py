"""
Escreva um programa que reflita essas mudanças e permita praticar com o conceito de listas. Sua tarefa:

etapa 1: criar uma lista vazia chamada beatles;
etapa 2: use o método append() para adicionar os seguintes membros da banda à lista: John Lennon, Paul McCartney e George Harrison;
etapa 3: Use o loop for e o método append() para solicitar que o usuário adicione os seguintes membros da banda à lista: Stu Sutcliffe e Pete Best;
etapa 4: use a instrução del para remover Stu Sutcliffe e Pete Best da lista;
etapa 5: Use o método insert() para adicionar Ringo Starr ao início da lista.

"""

beatles = []

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print(beatles)

for names in range(2):
    addnames = input("Add a member name: ")
    beatles.append(addnames)

print(beatles)
print(len(beatles))

i = 0 
for name in beatles:
    if name == "Pete Best" or name == "Stu Sutcliffe":
        del beatles[i]
        del beatles[i]
        print(beatles)
        print(len(beatles))
    i += 1

beatles.insert(0,"Ringo Starr")
print(beatles)