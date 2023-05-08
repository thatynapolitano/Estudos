secret_number = 93

number = int(input("Digite um número inteiro de 0-100: ")) 

while  number != secret_number: 
      print("Tente novamente!")
      number = int(input("Digite um número inteiro de 0-100: ")) 
      if number > 100:
         print("Digite apenas números inteiros de 0 - 100.")   
      else:
           ("Digite apenas números inteiros de 0 - 100.")
print("Acertou!")