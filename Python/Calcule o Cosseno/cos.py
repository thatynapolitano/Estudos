from numpy import pi
from math import factorial
x_graus=float(input('Informe o valor do ângulo, em graus: '))
x_radianos=pi*x_graus/180
cos=0
for n in range(10):
  cos=cos+(-1)**n*x_radianos**(2*n)/factorial(2*n)
print(cos)
