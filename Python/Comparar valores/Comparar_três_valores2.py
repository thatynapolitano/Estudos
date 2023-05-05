num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
num3 = int(input("Digite um numero: "))

if num1 == num2 == num3:
    print("Os numeros digitados são iguais, logo o número identificado é o maior")
elif num1 > num2 and num1 > num3:
    print(f"Numero {num1} é maior que numero {num2} e {num3}") 
elif num2 > num1 and num2 > num3:
    print(f"Numero {num1} é maior que numero {num3}")
else:
    print(f"Numero {num3} é maior que todos")