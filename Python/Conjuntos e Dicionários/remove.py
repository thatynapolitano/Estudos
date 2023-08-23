# ().REMOVE

numeros = {1,2,3,4,5,6,7,8,9,10}

numeros.remove(1)
print(numeros)

# É muito parecido com o método ().DISCARD 
# A unica diferença é que quando passo um parametro que não existe no método DISCARD, ele simplesmente ignora a ação. 
# Porém quando passo um parametro que não existe no método REMOVE, ele vai dar um Key Error apontando o parametro que não existe. Veja o exemplo abaixo: 

numeros.remove(11)
print(numeros)