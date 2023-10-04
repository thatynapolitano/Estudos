# Calculadora de IMC 

def calculadora_imc():
    altura = float(input("Digite a sua altura aqui: "))
    peso = float(input("Digite o seu peso aqui: "))


    IMC = peso / altura ** 2 
    print(f"O seu IMC é: {IMC:.2f}") 


    if IMC < 18.5: 
        print("Abaixo do peso")
    elif IMC >= 18.6 and IMC <= 24.9:
        print("Peso ideal (Parabéns!)")
    elif IMC >= 25 and IMC <= 29.9:
        print("Levemente acima do peso")
    elif IMC >= 30 and IMC <= 34.5:
        print("Obesidade Leve (grau I)")
    elif IMC >= 35 and IMC <= 39.9:
        print("Obesidade Severa (grau II)")
    else:
        print("Obesidade Mórbida (grau III)")


calculadora_imc()