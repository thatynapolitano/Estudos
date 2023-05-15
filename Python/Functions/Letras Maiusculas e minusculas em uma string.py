# letra = "D"

# letra.islower()
# letra.isupper()



# Exercício 5- Escreva uma função que imprima quantas letras em uma string recebida por parâmetro são maiúscula e quantas são minúsculas.
texto = "Super Mario Bros"
letrasMaiusculas= 0

for caractere in texto:
    if caractere.isupper():
        letrasMaiusculas += 1
print(f"No texto tem {letrasMaiusculas} letras maisculas.") 

# Outra forma:

texto = 'Super Mario Bros'

letrasMaiusculas=0
letrasMinusculas=0
for caractere in texto:
  if caractere.isupper():
    letrasMaiusculas+=1
  elif caractere.islower():
    letrasMinusculas+=1

print("Maiusculas:",letrasMaiusculas)
print("Maiusculas:",letrasMinusculas)

# Colocar isso em uma função

def contaMaiusculaMinuscula(texto):
  letrasMaiusculas=0
  letrasMinusculas=0
  for caractere in texto:
    if caractere.isupper():
      letrasMaiusculas+=1
    elif caractere.islower():
      letrasMinusculas+=1

  print("Maiusculas:",letrasMaiusculas)
  print("Maiusculas:",letrasMinusculas)

msg = 'Super Mario Bros'
contaMaiusculaMinuscula(msg)
msg = '123456'
contaMaiusculaMinuscula(msg)
    
