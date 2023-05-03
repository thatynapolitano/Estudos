#Considere o vetor v que armazena os preços de venda, em dólares, de algumas mercadorias anunciadas em um comércio eletrônico:

# v=(138,40; 86,70; 90,90; 234,90; 107,70). 

# Supondo que cada dólar corresponde a R$ 5,10, obtenha por meio do Python o vetor u que contém os preços destas mercadorias em reais.

import numpy as np 
v=np.array([[138.40, 86.70, 90.90, 234.90, 107.70]]) 
u=5.10*v 
print(u)
