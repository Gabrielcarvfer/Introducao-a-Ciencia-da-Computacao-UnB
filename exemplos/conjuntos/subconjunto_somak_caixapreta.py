


def caixa_preta(vetor, soma_desejada):
    somaTemp = 0
    for elemento in vetor:
        somaTemp += elemento
        if somaTemp == soma_desejada:
            return True

    return False


def subset_soma_k(vetor, k, n):

    existe_solucao = caixa_preta(vetor, k)

    if not existe_solucao:
        return False

    if n == 0:
        return vetor
    else:
        vetTemp = vetor
        A = list(vetor[:-1])
        if caixa_preta(A,k):
            vetTemp = A
        return subset_soma_k(vetTemp, k, n-1)

def main():
    vetor = [1, 4, 7, 3, 2, 6, 8, 5, 9, 10]
    soma_k = 15
    subset = subset_soma_k(vetor,soma_k, len(vetor))
    print(subset)

main()