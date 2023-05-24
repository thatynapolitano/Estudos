#Lista com dicionários dentro

jogo1 = {'Nome':'Super Mario','videogame':'SNES','Ano':1990}
jogo2 = {'Nome':'Mario Kart 64','videogame':'N64','Ano':1998}
jogo3 = {'Nome':'Pokemon Yellow','videogame':'GameBoy','Ano':1999}

listaJogos = [jogo1,jogo2,jogo3]
print(listaJogos[1]["Nome"]) # Vai imprimir Mario Kart 64.

#Para acessar o último elemento de uma lista 
print(listaJogos[-1])