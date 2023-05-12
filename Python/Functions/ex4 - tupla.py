def contaDupla(x,y):
  soma=x+y
  mult=x*y
  return (soma,mult)

resp1,resp2 = contaDupla(10,20) # TUPLA -> Tuplas são similares a listas, isto é, uma sequência de dados de qualquer tipo. Porém, ao contrário de listas, as tuplas são imutáveis. Tuplas são representadas por uma sequência de valores separados por vírgula, e entre um abre e fecha parênteses. 
print(resp1,resp2)

# outra forma 

def calcular(x,y,op):
  if op=='*':
    return x*y
  elif op=='+':
    return x+y


resposta = calcular(10,20,'*')
print(resposta)
