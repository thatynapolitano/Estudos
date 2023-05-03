#isso, se o valor de X for menor que a média muda a linha 

#"p=0.5-scipy.stats.norm(media,desvio_padrao).cdf(X)"

#Se o valor de X for maior que a média fica 

#"p=scipy.stats.norm(media,desvio_padrao).cdf(X)-0.5" 


import scipy.stats

media = 90000
desvio_padrao = 4000
X= 95000

p=scipy.stats.norm(media,desvio_padrao).cdf(X)-0.5
print(p)


import scipy.stats
media=5000
desvio_padrao= 300
X= 5500
p=scipy.stats.norm(media,desvio_padrao).cdf(X)-0.5
print(p)

