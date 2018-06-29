

def concatena(metade_esquerda, metade_direita):
    vetorTemp = []

    esquerda_indice = 0
    direita_indice  = 0

    for k in range(len(metade_esquerda)+len(metade_direita)):
        if direita_indice <= len(metade_direita) and esquerda_indice <= len(metade_esquerda):
            if metade_esquerda[esquerda_indice] <= metade_direita[direita_indice]:
                vetorTemp.append(metade_esquerda[esquerda_indice])
                esquerda_indice += 1

            else:
                vetorTemp.append(metade_direita[direita_indice])
                direita_indice += 1

        if direita_indice >= len(metade_direita):
            vetorTemp += metade_esquerda[esquerda_indice:]
            break
        if esquerda_indice >= len(metade_esquerda):
            vetorTemp += metade_direita[direita_indice:]
            break

    return vetorTemp

def mergesort(vetorEntrada):

    #Se o vetor tiver um único elemento, já está ordenado
    if len(vetorEntrada) <= 1:
        return vetorEntrada

    #Se o vetor tiver mais de um elemento, ou j-i > 1, parte em dois pedaços e repete recursivamente
    meio = len(vetorEntrada) // 2

    metade_esquerda = mergesort(vetorEntrada[:meio])
    metade_direita = mergesort(vetorEntrada[meio:])

    #Após ordenar os dois pedaços esquerdo e direito do subvetor vetorEntrada[i:j], concatena os pedaços
    subVetorOrdenado =  concatena(metade_esquerda, metade_direita)
    return subVetorOrdenado

def main():
    vetorEntrada = [9, 2, 3, 7, 5, 1, 4, 8, 6]

    vetorOrdenado = mergesort(vetorEntrada)
    print(vetorEntrada)
    print(vetorOrdenado)
    return

main()