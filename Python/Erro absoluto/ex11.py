#O erro absoluto é o módulo da diferença entre o valor exato e o valor aproximado:

# E_A=|x-▁x|

# onde x é o valor exato e ▁x é o valor aproximado e o erro relativo é a divisão do módulo da diferença entre o valor exato e o valor aproximado pelo módulo do valor exato:

# E_R=(|x-▁x|)/(|x|),x≠0.

#Considerando um problema onde o valor exato de uma variável corresponde a 0,5672 e o valor aproximado é 0,55. Qual é o erro absoluto e qual é o erro relativo? Utilize o Python.



x1 = 0.5672 #Valor exato
x2 = 0.55 #Valor aproximado 

#Erro absoluto 

def AbsoluteError (x1,x2):
    Result = (x1 - x2)
    return Result

Answer = AbsoluteError(0.5672, 0.55)
print(Answer)

# Erro Relativo

def RelativeError (x1,x2):
    Result2 = (x1 - x2) / x1 
    return Result2

Answer2 = RelativeError(0.5672, 0.55)
print(Answer2)
