# Considere os números a=7,0102x105 e b=2,1233x103 na notação científica normalizada. Por meio do Python, calcule a*b apresentando o resultado com 10 casas decimais.

#Numero em notação cientifica  
num = 701020.0
print(f'{num:e}') 

#Numero em notação cientifica  
num2 = 2123.3
print(f'{num2:e}')  

#Função que multiplica dois números
def Multi(num, num2):
    Resultado = num * num2 
    return Resultado 

Multiplicacao = Multi(701020.0, 2123.3)
print(Multiplicacao) 

#Resultado de a*b (num * num2) para notação cientifica com 10 casas decimais:
num3= 1488475766.0000002
print(f'{num3:.10e}')