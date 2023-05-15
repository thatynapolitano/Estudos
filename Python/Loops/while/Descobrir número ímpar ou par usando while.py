
# Para saber se um número é par ou ímpar usando while

c0 = int(input("Digite um número inteiro diferente de 0 (digite 0 apenas para encerrar o programa):  " ))

while c0 != 0:
    if c0 %2 == 1:
        print("O número é impar")
        c0 += 1
    elif c0 == 0:
        break
    else: 
        print("O número é par")
        c0 += 1
    c0 = int(input("Digite um número inteiro diferente de 0: "))

print("O programa foi encerrado")