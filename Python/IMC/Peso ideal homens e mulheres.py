estatura = float(input("Insira a sua estatura em metros: "))
genero = input("Insira o seu gênero: ") 

homens = (72.7 * estatura) - 58 
mulheres = (62.1 * estatura) - 44.7

if genero == "h" or genero == "H":
    print("O seu peso ideal é:", homens)
elif genero == "m" or genero == "M":
    print("O seu peso ideal é:", mulheres)
else: 
    print("ERROR - Not found") 

    #Outra forma 

print('Calcule seu peso ideal')
print('-----------------------')
alt = float(input('Digite sua altura: '))
print('Informe seu sexo')
sexo= input('Digite "m" para masculino e "f" para feminino: ').lower()

#lowercase minusculo
#uppercase maiusculo

if sexo == "m":
    peso= (72.7 * alt) - 58
    print ("Seu peso ideal é:", peso)
elif sexo == "f":
    peso=  (62.1 * alt) - 44.7 
    print ("Seu peso ideal é:", peso)
else:
    print('Deu erro!')