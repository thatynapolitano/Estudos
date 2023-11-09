soma = 0 #meu inicializador começa com 0 

for i in range (1, 4): # Quantidade de vezes da minha repetição é 3. O primeiro argumento é o inicio e o segundo argumento é o final do meu range que no caso é 3.
    nota=float(input(f"Informe sua nota {i}: ")) # Vou pedir para o usuário inserir 3 notas. 
    soma = soma + nota #Gravo por vez cada nota que o usuário digita e itero com o meu inicializador "soma" para fazer a soma dos números.
print(soma/3) # Aqui imprimo a soma dos números e já faço a média aritmetica, divindo por 3. 

# OBS: a função range recebe 3 parametros, (inicial, final, steps)
# Quando recebe 1 parametro: (10) -> A quantidade de vezes que o meu laço irá se repetir, que nesse caso, é 9. 
# Quando recebe 2 parametros: (2,10) -> Inicio e fim do range
# Quando recebe 3 parametros: (3,12,3) -> Inicio, fim do range e passos (steps = pulando de 3 em 3)

