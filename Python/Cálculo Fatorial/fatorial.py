def fatorial(N):
    if N < 0: 
        return None
    elif N == 0:
        return 1
    else:
        fat = 1 
        print(fat)
        for i in range(1,N+1):
            print(fat)
            fat *= i 
        return fat

print(fatorial(4))

# Fatorial de 4 =  4*3*2*1

while True:

    try: 
        num = int(input("Informe o número que deseja o fatorial: "))
        if num < 0:
            print("O número precisa ser positivo!")
            continue 
        else: 
            break
    except:
        print("O numero deve ser inteiro! Tente novamente")

fat = fatorial(num)
print(f"O fatorial de {num} é {fat}")
    