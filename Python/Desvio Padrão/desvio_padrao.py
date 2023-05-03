import pandas as pd
x={'Pesos':[48.8, 48.9, 49.0, 49.1, 49.2, 49.3,
49.5, 49.7, 49.7, 49.7, 49.8, 50.0, 50.1, 50.1,
50.2, 50.2, 50.4, 50.6, 50.8, 50.9]}
p=pd.DataFrame(x)
desviopadrao=p['Pesos'].std()
print(f'Desvio padrão: {desviopadrao}')