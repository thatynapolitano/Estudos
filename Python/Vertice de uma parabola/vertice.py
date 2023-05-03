# Uma função quadrática y= 10x²- 150x + 30
# Calcule o vertice de x e y 
a = 10
b = -150
c = 300

xv = -b / (2 * a)
yv = a * xv ** 2 + b * xv + c

print("Coordenadas do vertice: ({}, {})".format(xv, yv))
