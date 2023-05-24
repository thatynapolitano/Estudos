#{'cidade':'curitiba','latitude':-25.2548,'longitude':-49.1615}  <= exemplo de como ficará nosso dicionário 

listaCidades=[]
cidade = {}

#leitura das cidades, nome vazio encerra
nome = input("Dgite o nome da cidade: ")
while nome != "":
    cidade["nome"]=nome
    cidade["latitude"]=float(input("Latitude"))
    cidade["longitude"]=float(input("Longitude"))    
    listaCidades.append(cidade.copy()) # Não esquecer de sempre adicionar uma cópia, para não subscrever as informações anterior e perdê-las
    nome = input("Digite o nome da cidade")

print(listaCidades)

#Colocando em ordem crescente por latitude e longitude.

listaSulNorte = sorted(listaCidades,key=lambda dicionario:dicionario["latitude"])  # A função sorted ordena a minha listaCidades se tivessemos apenas uma informação. Porém o sorted não ordena da forma específica o que queremos por si só, principalmente quando temos várias informações diferentes. Por isso adicionamos key=lambda dicionario:dicionario["latitude"]. Lambda é uma forma de criar uma função de uma linha no formato entrada e saída. Uma função dicionário que sai a latitude do dicionário -> Ou seja função com entrada e saída. A entrada é dicionario e a saída é latitude de dicionário. Por isso dicionario:dicionario["latitude"]. 

listaOesteLeste = sorted(listaCidades,key=lambda dicionario:dicionario["longitude"]) # A função sorted ordena a minha list

norte = listaSulNorte[-1]['Nome']
sul = listaSulNorte[0]['Nome']
leste =listaOesteLeste[-1]['Nome']
oeste = listaOesteLeste[0]['Nome']

print()

