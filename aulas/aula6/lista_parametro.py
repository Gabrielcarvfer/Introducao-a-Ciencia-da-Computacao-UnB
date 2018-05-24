#função modificadora
def muda_lista(lista):
    print("Função modificadora")
    print(lista)

    lista[0] = 0

    print(lista)
    print()


#função pura
def nao_muda_lista(lista):
    print("Função não modificadora")

    lista_temporaria = list(lista)
    lista_temporaria[0] = 1

    print(lista)
    print(lista_temporaria)
    print()

#ordena lista
def merge_sort(lista_numeros):
    if len(lista_numeros) == 1:
        return lista_numeros

    metade_esquerda_ordenada = merge_sort(lista_numeros[:int(len(lista_numeros)//2)])
    metade_direita_ordenada  = merge_sort(lista_numeros[len(lista_numeros)//2:])

    #concatena resultados ordenados
    lista_numeros_ordenados_concatenado = []
    while len(lista_numeros_ordenados_concatenado) < len(lista_numeros):
        if len(metade_direita_ordenada) > 0 and len(metade_esquerda_ordenada) > 0:
            if metade_esquerda_ordenada[0] < metade_direita_ordenada[0]:
                lista_numeros_ordenados_concatenado.append(metade_esquerda_ordenada[0])
                metade_esquerda_ordenada.pop(0)
            else:
                lista_numeros_ordenados_concatenado.append(metade_direita_ordenada[0])
                metade_direita_ordenada.pop(0)
        else:
            lista_numeros_ordenados_concatenado += metade_esquerda_ordenada + metade_direita_ordenada
    return lista_numeros_ordenados_concatenado

#função modificadora de ordenação
def bubble_sort(lista_numeros):
    for i in range(0, len(lista_numeros)):
        for j in range(0,len(lista_numeros)-1):
            if lista_numeros[j] > lista_numeros[j+1]:
                temp = lista_numeros[j+1]
                lista_numeros[j+1] = lista_numeros[j]
                lista_numeros[j] = temp

def main():
    uma_lista = [1,2,3,"abc"]
    muda_lista(uma_lista)
    nao_muda_lista(uma_lista)

    lista_numeros = [7,6,5,4,3,2,1,0]
    lista_ordenada = merge_sort(lista_numeros)

    print("Ordenação MergeSort")
    print(lista_numeros)
    print(lista_ordenada)
    print()
#
    print("Ordenação BubbleSort")
    bubble_sort(lista_numeros)
    print(lista_numeros)


main()