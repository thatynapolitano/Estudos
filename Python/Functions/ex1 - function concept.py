# Função é um bloco de código identificado po um nome e pode receber uma lista de parametros, esses parametros podem ou não ter valores padrões. Usar funções torna o código mais legível e possibilita o reaproveitamento de código. Programas baseado em funções, é o mesmo que dizer que estamos programando de maneira estruturada.



# Forma 1 
print('|',"-"*18,'|')
print('|',"-"*18,'|')
print('         MENU')
print('|',"-"*18,'|')
print('|',"-"*18,'|')

# Forma 2 com função 
def darDestaque():
  print('|',"-"*18,'|')
  print('|',"-"*18,'|')

darDestaque()

# Forma 3 com função 

def darDestaque():
  print('|',"-"*18,'|')
  print('|',"-"*18,'|')

darDestaque()
print('        MENU')
darDestaque()

# Forma 4 com função 

def darDestaque(palavra):
  print('|',"-"*18,'|')
  print('|',"-"*18,'|')
  print('        ',palavra)
  print('|',"-"*18,'|')
  print('|',"-"*18,'|')


darDestaque('MENU')
darDestaque('LISTA DE COMPRAS')

# Outro exemplo 
def darDestaque(palavra,qtd): #Definição da função darDestaque
  print('|',"-"*18,'|')
  print('|',"-"*18,'|')
  for i in range(qtd):
    print('        ',palavra)
  print('|',"-"*18,'|')
  print('|',"-"*18,'|')


darDestaque('Mario',3)

# Outro

def borda(palavra): #Definição da função darDestaque
  tamanho = len(palavra)  #length
  print('+',"-"*tamanho,'+')
  print('|',palavra,'|')
  print('+',"-"*tamanho,'+')


borda('Mario')

borda('Lógica de Programação e Algoritmos')