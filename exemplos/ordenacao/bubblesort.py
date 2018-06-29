def bubblesort(vetorEntrada):
    vetorSaida = list(vetorEntrada)

    for i in range(len(vetorEntrada)):
        for j in range(i,len(vetorEntrada)):
            if vetorSaida[i] > vetorSaida[j]:
                temp = vetorSaida[i]
                vetorSaida[i] = vetorSaida[j]
                vetorSaida[j] = temp

    return vetorSaida



def main():
    vetorEntrada = [9, 2, 3, 7, 5, 1, 4, 8, 6]

    vetorOrdenado = bubblesort(vetorEntrada)
    print(vetorEntrada)
    print(vetorOrdenado)
    return

main()