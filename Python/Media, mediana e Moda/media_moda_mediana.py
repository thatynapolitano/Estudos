import pandas as pd
x={'Pesos':[48.8, 48.9, 49.0, 49.1, 49.2, 49.3, 49.5, 49.7, 49.7, 49.7, 49.8, 50.0, 50.1, 50.1, 50.2, 50.2, 50.4, 50.6, 50.8, 50.9]}
p=pd.DataFrame(x)
media=p['Pesos'].mean()
moda=p['Pesos'].mode()
mediana=p['Pesos'].median()
print(f'Média: {media}')
print(f'Moda: {moda}')
print(f'Mediana: {mediana}')