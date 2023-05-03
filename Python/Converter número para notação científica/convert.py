# Converter um numero para notacao cientifica com 8 casas decimais 
num = 458189 
print(f'{num:.8e}') 

# Exemplo 
# print('{:e}'.format(número))
# 1.234568e+08

# Ou pode utilizar as próprias f-strings:
# número = 123456789.123456
# print(f'{número:e}')
# 1.234568e+08 

# Se precisar limitar o número de casas decimais, pode fazer:

# número = 123456789.123456
# print(f'{número:.2e}')
# 1.23e+08

num = 70102
print(f'{num:.5e}')

num = 21233
print(f'{num:.3e}')
