#Listas trabalham com Referência
x=[10,20,30,40,50]
y=x  #referência
#y=x[:] #copia
x[0]=100
print(x)
print(y)

#Listas primitivas trabalham com cópia
x=100
y=x
y+=10
print(x,y)