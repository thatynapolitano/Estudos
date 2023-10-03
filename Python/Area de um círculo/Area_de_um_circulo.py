#Cacule a área do circulo com raio 10:

# 1 forma de fazer sem usar biblioteca
raio = float(input('Digite o raio do circulo: '))
area = 3.1415 * raio*raio
print(f'A área é: {area:.2f}') # :.2f para diminuir para duas casas decimais o resultado 

# 2 forma de fazer usando biblioteca
import math 
raio = float(input('Digite o raio do circulo: '))
area = math.pi * raio**2  
print(f'A área é: {area:.2f}')  


