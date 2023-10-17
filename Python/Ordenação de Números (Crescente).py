entrada = input("Digite os 4 números separados por vírgula: ")

numeros = [int(x) for x in entrada.split(',')]

# Ordena os números usando condicionais
if numeros[0] > numeros[1]:
    numeros[0], numeros[1] = numeros[1], numeros[0]
if numeros[1] > numeros[2]:
    numeros[1], numeros[2] = numeros[2], numeros[1]
if numeros[2] > numeros[3]:
    numeros[2], numeros[3] = numeros[3], numeros[2]

# Verifica e corrige a ordem dos números negativos, se necessário
if numeros[0] > numeros[1]:
    numeros[0], numeros[1] = numeros[1], numeros[0]
if numeros[2] > numeros[3]:
    numeros[2], numeros[3] = numeros[3], numeros[2]

print("Sua lista ordenada é:", numeros)
