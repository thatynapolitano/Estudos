# Tuplas são estruturas de dados muito parecidas com as listas, a principal diferença é que tuplas são imutáveis enquanto listas são mutáveis.
# Podemos criar tuplas através da classe tuple, ou colocando valores separados por vírgula de parenteses.

frutas = ("laranja", "pera", "uva",)  #É sempre bom colocar uma virgula no final como boa pratica, para o python identificar como tupla. 

# Para percorrer a tupla:
frutas[0]
frutas[2]

letras = tuple("python")

numeros = tuple([1, 2, 3, 4])

pais = ("Brasil")

# Tuplas aninhadas 
# Tuplas podem armazenar todos os tipos de objetos Python, portanto podemos ter tuplas que armazenam outras tuplas. 
# Com isso podemos criar estruturas bidimensionais (tabelas), e acessar informando os índices de linha e coluna. 

matriz = [
    [1, "a",2],
    ["b", 3, 4],
    [6, 5, "c"]
]

matriz[0] # [1, "a", 2]
matriz[0][0] # 1 
matriz[0][-1] # 2
matriz[-1][-1] # "c"


