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