# Classificação de times, exemplos:

def classificacao(pontuacao):
  ouro = range(180, 201)
  prata = range(150, 180)
  bronze = range(110, 150)
  mention = range(50, 110)

  if pontuacao in ouro:
    print('O time recebeu a medalha de ouro!')
  elif pontuacao in prata:
    print('O time recebeu a medalha de prata!')
  elif pontuacao in bronze:
    print('O time recebeu a medalha de bronze!')
  elif pontuacao in mention:
    print('O time recebeu uma menção honrosa!')
  else: 
    print('O time não se classificou!')

pontos = int(input('Digite a pontuação do time: (zero para encerrar)'))
while pontos != 0:
  classificacao(pontos)
  pontos = int(input('Digite a pontuação do time: (zero para encerrar)'))