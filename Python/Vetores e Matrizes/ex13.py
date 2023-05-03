# 13) Dados os vetores
# u=(3, 6, -1) e v=(11, 14, 9)
# obtenha por meio do Python o vetor w=u.v.
  

import numpy as np 
u=np.array([[3, 6,-1]])
v=np.array([[11, 14, 9]])
w=np.inner(u, v)
print(w)