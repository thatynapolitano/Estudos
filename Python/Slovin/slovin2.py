from math import ceil
N=150000
e=0.02
n=ceil(N/(1+N*e**2))
print(f'Tamanho da amostra: {n}')