# Obter da entrada padrao massa, estatura e imprima o IMC (indice de massa corporea). Massa em quilogramas dividido pela estatura em metros. 

massa = float(input("Digite aqui a sua massa em kg: "))
estatura = float(input("Digite aqui a sua estatura em metros: "))

IMC = massa / estatura**2 
print(f"O seu IMC é: {IMC:.2f}")
