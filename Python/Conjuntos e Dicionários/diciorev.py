frase = "a palavra dada dita por mim é igual a palavra dita por ele"
listaPalavras = frase.split() #separa a string em lista utilizando o separador ' ' por padrão
dicionario ={} #chave: a palavra em si; valor: sua contagem

for palavra in listaPalavras:
  dicionario[palavra] = dicionario.get(palavra,0) +1

#metodo items, coloca no formato lista de tuplas(chave,valor)
for palavra, ocorrencias in dicionario.items():
  print(palavra,':',ocorrencias)
