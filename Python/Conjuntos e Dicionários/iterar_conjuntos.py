# A forma mais comum para percorrer os dados de um conjunto é utilizadno o comando for.

carros = {"gol", "celta", "palio"}

for carro in carros: 
    print(carro)


# Para saber qual posição está os elementos da minha lista (o indice)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")