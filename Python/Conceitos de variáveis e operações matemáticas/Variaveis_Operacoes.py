#A cerquilha eh como colocamos comentários. Da cerquilha em diante a linha é ignorada. Não é lida pelo computador.

print('Alo fulano!') #Mostra a mensagem 
print('Alo ciclano!') #Mostra a mensagem 

#Comandos básicos: 
#Variáveis = São espaços reservados na memória (que possuem apelidos) para armazenar informações que podemos utilizar no futuro. 

#Variáveis numéricas 
idade = 21 
peso = 49.5 #No python numero decimal é usando ponto. Como no inglês. Não usa vírgula. 

#Variáveis de strings:
nome = 'Mario'
endereco = 'Rua dos cogumelos, 274' 
print('Seja bem vindo', nome, 'seu produto sera enviado para', endereco) 

#formas de imprimir com dados 
print('Oi', nome, 'sua idade eh' , idade,'. Parabens!') 
print('Ola {} sua idade eh {} . Parabens!'.format(nome,idade))
print(f'Ola {nome} sua idade eh {idade} . Parabens!')

#operacoes
print(2+3)
print('2+3')
print('2'+'3') #Concatenacao 
print('Ola'+'Mundo' ) #Concatenacao

#operacoes aritmeticas basicas 
print(2+5) #soma
print(4-1) #subtracao
print(5*2) #multiplicacao
print(7/2) #divisao real, trabalha com numeros decimais
print(7//2) #divisao inteira, trabalha apenas com numeros inteiros
print(7%2) #resto de divisao (mod) le-se: 7 mod 2 
print(3**2) #exponenciacao
#print(math.sqrt(9)) #raiz quadrada (biblioteca)

valorA = 10-7 
valorB = (10*4)-4 
valorA = valorA**2
valorC = valorA+valorB+1 
print('O resultado final eh', valorC) 

#Leitura de dados
nome = input('Digite seu nome:')
print('Seja bem-vindo', nome)

idade = input('Digite sua idade: ') #idade em texto
idade=int(input('Digite sua idade: ')) #idade em numero precisa colocar o int = integer = inteiro 
print('No ano que vem voce tera', idade+1)

peso = float(input('Digite seu peso:')) #Float = ponto flutuante = trabalha com numeros reais (numeros decimais) 
print(f'Seu peso eh: {peso}')