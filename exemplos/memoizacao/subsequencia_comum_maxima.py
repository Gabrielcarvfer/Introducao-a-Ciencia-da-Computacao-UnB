sequencia1 = [-10, 20, 10, -30, 40]
sequencia2 = [ 80, 20, 10, -70, 30]

#Valores subsequências para sequência 1
#Subsequências de tamanho 1
# [0] = -10
# [1] =  20
# [2] =  10
# [3] = -30
# [4] =  40

#Subsequências de tamanho 2
# [0,1] =  10
# [1,2] =  30
# [2,3] = -20
# [3,4] =  10

#Subsequências de tamanho 3
# [0,1,2] =  20
# [1,2,3] =   0
# [2,3,4] =  20

#Subsequências de tamanho 4
# [0,1,2,3] =  40
# [1,2,3,4] =  40

#Subsequências de tamanho 5
# [0,1,2,3,4] = 80

#precalcula soma subsequencias da lista 1
somaSeqList1 = [[] for i in range(len(sequencia1)+1)]

seqTemp = list(sequencia1)
while len(seqTemp) > 0:
    tempSoma = 0
    tempSeq = []

    for elemento in seqTemp:
        tempSeq.append(elemento)
        tempSoma += elemento
        somaSeqList1[len(tempSeq)].append((list(tempSeq), tempSoma))

    seqTemp.pop(0)

#precalcula soma subsequencias da lista 2
somaSeqList2 = [[] for i in range(len(sequencia2)+1)]

seqTemp = list(sequencia2)
while len(seqTemp) > 0:
    tempSoma = 0
    tempSeq = []

    for elemento in seqTemp:
        tempSeq.append(elemento)
        tempSoma += elemento
        somaSeqList2[len(tempSeq)].append((list(tempSeq), tempSoma))

    seqTemp.pop(0)

#busca subsequencia na outra sequencia


def busca_subsequencia(seq1, seq2):

    #Copia sequência 1
    seq = list(seq1)

    #Busca recursiva
    for i in range(len(seq1)):
        seq.pop(0)
        busca_subsequencia(seq, seq2)

    for j in range(len(seq2)):

busca_subsequencia(sequencia1, sequencia2)

pass


