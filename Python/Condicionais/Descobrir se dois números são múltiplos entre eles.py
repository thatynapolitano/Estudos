a = float(input("Coloque um numero aqui: "))
b = float(input("Coloque um numero aqui: "))

if a % b == 0 or b % a == 0:
    print(f"{a} e {b} são multiplos")
else: 
    print (f"O número {a} e {b} não são multiplos")
