def iniciais(nome,sobrenome):
  letrasIniciais = ''
  letrasIniciais+= nome[0].upper()
  letrasIniciais+= '. '
  letrasIniciais+= sobrenome[0].upper()
  letrasIniciais+= '.'
  return letrasIniciais

nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')

print('Suas iniciais são', iniciais(nome,sobrenome))

#OUTRA FORMA

nome = input('Digite Nome: ')
sobrenome = input('Digite Sobrenome: ')

print(nome[0]+'.',sobrenome[0]+'.')