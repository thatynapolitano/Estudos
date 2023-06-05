#Exercicio 10 
#Leia as coordenadas de 2 pontos: 
# Ponto1: x1, y1; 
# Ponto2: x2, y2; 
# Calcule e mostre o ponto médio e diga em qual quadrante o ponto está localizado. 

x1 = int(input("X1: "))
y1 = int(input("Y1: "))
x2 = int(input("X2: "))
y2 = int(input("Y2: "))

#Média dos pontos
x3 = (x1 + x2) / 2
y3 = (y1 + y2) / 2

if x3 == 0 or y3 == 0:
    print("Está em um dos eixos")
elif x3 >= 1 and y3 >= 1:
    print("A coordenada dos pontos está no quadrante 1")
elif x3 <= -1 and y3 >= 1:
    print("A coordenada dos pontos está no quadrante 2")
elif x3 >= -1 and y3 >= -1:
    print("A coordenada dos pontos está no quadrante 3")
else: #x3 <= -1 and y3 <= 1
    print("A coordenada está no quadrante 4")


