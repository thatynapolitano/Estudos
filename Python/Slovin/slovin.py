def CalculoSlovin(Numero, e):
    Resultado = Numero / (1 + Numero*e**2)
    return Resultado

Tamanho_Amostra = CalculoSlovin(150000, 0.02)
print(Tamanho_Amostra)
