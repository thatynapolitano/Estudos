"""
Em 1937, um matemático alemão chamado Lothar Collatz formulou uma hipótese intrigante (ainda não comprovada) que pode ser descrita da seguinte forma:

pegue qualquer número inteiro diferente de zero e diferente de zero e nomeie-o como c0;
se for par, avalie um novo c0 como c0 ÷ 2;
caso contrário, se for ímpar, avalie um novo c0 como 3 * c0 + 1;
se c0 ≠ 1 , volte ao ponto 2.
A hipótese diz que, independentemente do valor inicial de c0, ela sempre vai para 1.

"""


c0 = float(input('Digite um numero inteiro: '))

while c0 != 1 and c0 != 0:
    if c0 %2 == 0:
        c0 = c0 / 2 
        print(c0)
    elif c0 %2 == 1: 
        c0 = 3 * c0 + 1 
        print(c0)
