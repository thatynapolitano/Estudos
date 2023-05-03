#Descobrir a altura de um predio sabendo que uma bola de metal é solta do topo desse predio e um cronometro marcou 3 segundos de queda. Assuma a aceleracao da gravidade como sendo 9.8 
#Depois adapte seu programa para funcional com um numero qualquer de segundos informado pelo usuario. 

gravidade = float(input("Insira aqui o valor da gravidade: "))
tempo = float(input("Tempo em que o objeto demorou para cair do topo do predio: "))
distancia = (gravidade * tempo **2) / 2
print(f"A distancia eh: {distancia}")