#Matrizes

# Exemplo 1)

#import numpy as np
#A=np.array([[3, 2, -1], [5, 0, 20]])
#print(A) 

# Exemplo 2)

#import numpy as np
#F1=np.array([[400, 10], [480, 12], [600, 15]])
#F2=np.array([[31, 11], [37, 11], [48, 11]])
#CustoTotal=F1+F2 
#print(CustoTotal)

# Exemplo 3)

import numpy as np
A=np.array([[3, 1, 3], [6, 5, 5]])
B=np.array([[100, 50], [50, 100], [50, 50]])
C=np.matmul(A,B)  
print(C)