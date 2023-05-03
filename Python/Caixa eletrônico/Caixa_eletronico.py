# Um caixa eletronico emite cedulas/notas de 100, 50, 20, 5, 1 reais. Qual a quantidade minima de notas que esse caixa vai emitir de cada cedula, dependendo do valor de saque que o cliente quer realizar? (1999,183)

#1999 

valor = int(input("Digite o valor que deseja sacar: "))
notas100= valor//100
valor%=100 #valor= valor%100  redefini a variavel valor, o valor fica 99. 
notas50= valor//50 
valor%=50 # valor = 49
notas20= valor//20
valor%=20 # valor =9 
notas5= valor//5 
valor%=5 # valor = 4 
notas1= valor  
print(f"Notas 100 = {notas100}")
print(f"Notas 50 = {notas50}")
print(f"Notas 20 = {notas20}")
print(f"Notas 5 = {notas5}")
print(f"Notas 1 = {notas1}")