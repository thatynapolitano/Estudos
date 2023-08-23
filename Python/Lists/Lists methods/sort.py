# O metodo sort quando eu quero ordenar minha lista na ordem alfabetica

linguagens = ["python","js", "c", "java", "c#"] 
linguagens.sort() 

print(linguagens)

# Dentro de sort eu posso passar um arumento reverse  e key

linguagens = ["python","js", "c", "java", "c#"] 
linguagens.sort(reverse=True) 

linguagens = ["python","js", "c", "java", "c#"] 
linguagens.sort(key=lambda x: len(x)) # ["c", "js", "java", python", "c#"]

linguagens = ["python","js", "c", "java", "c#"] 
linguagens.sort(key=lambda x: len(x), reverse=True) # ["python", "c#", "java", "js", "c"]
