# Conjuntos em Python não suportam indexação e nem fatiamento, caso queira acessar os seus valores é necessário converter o conjunto para lista.

numeros = {1, 2, 3, 2}

numeros = list(numeros) #conversão de conjunto para lista

numeros[0]

print(numeros[0]) 