"""Exercicio 1 - Crie um dicionario das duas listas abaixo
chaves = ["Dez","Vinte","Trinta"]
valores = [10,20,30]

Como fazer um dicionário que vá adicionando as informações na lista, por meio de um loop. Isso me pouparia trabalho de adicionar manualmente as infos.

"""
chaves = ['Dez', 'Vinte', 'Trinta']
valores = [10, 20, 30]

dicionario = {}
tam = len(chaves)

for i in range(tam):
  dicionario[chaves[i]] = valores[i]

print(dicionario)


