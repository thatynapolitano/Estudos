# def mergeSort(dados):
#     if len(dados) > 1:
#         meio = len(dados)//2
#         esquerda = dados[:meio]
#         direita = dados[meio:]
#         mergeSort(esquerda)
#         mergeSort(direita)
#         i = j = k = 0
#         while i<len(esquerda) and j<len(direita):
#             if esquerda[i]>direita[j]:
#                 dados[k]=esquerda[i]
#                 i=i+1
#             else:
#                 dados[k]=direita[j]
#                 j=j+1
#             k=k+1
#         while i<len(esquerda):
#             dados[k]=esquerda[i]
#             i=i+1
#             k=k+1
#         while j<len(direita):
#             dados[k]=direita[j]
#             j=j+1
            
# dados = [54, 26, 93, 17, 77, 31, 44, 55]
# mergeSort(dados)
# print(dados) 



def particao(lista, inicio, fim):
    pivot = inicio 
    for i in range(inicio+1, fim+1):
        if lista[i] <= lista[inicio]:
            pivot += 1
            lista[i], lista[pivot] = lista[pivot], lista[i]
    lista[pivot], lista[inicio] = lista[inicio], lista[pivot]
    return pivot

def quicksort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1
    if inicio < fim: 
        pivot_index = particao(lista, inicio, fim)
        quicksort(lista, inicio, pivot_index-1)
        quicksort(lista, inicio, pivot_index+1, fim)
        
        
MinhaLista = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(MinhaLista)
print(f"Lista ordenada: {MinhaLista}")