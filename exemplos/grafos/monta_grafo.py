INF = 99999999999999999999999999

from enum import Enum

class EstadoGrafo(Enum):
    NAO = 0
    PRIMEIRA_VEZ = 1
    SIM = 2


class Grafo():
    def __init__(self, indice = 0):
        self.indice = indice
        self.dist = INF
        self.vizinhos = {}
        self.visitado = EstadoGrafo.NAO
        self.caminho_da_raiz = []

def monta_grafo(lista_nos):
    grafo = {}

    for no in lista_nos:
        grafo[no[0]] = Grafo(no[0])

    for no in lista_nos:
        for no_adjacente in no[1]:
            grafo[no[0]].vizinhos[no_adjacente[0]] \
                = grafo[no_adjacente[0]].vizinhos[no[0]] = no_adjacente[1]

    return grafo

def um_teste_monta_grafo():
    lista_de_um_grafo = [[0,[]],
                         [1,[
                            [2,3],
                            [3,4],
                            [4,5],
                            ]],
                         [2,[
                             [4,2]
                            ]],
                         [3,[
                             [4,5],
                             [5,1],
                             [6,8],
                            ]],
                         [4,[
                             [5,4],
                            ]],
                         [5, [
                                [6, 9],
                             ]],
                         [6, [
                                [1, 7],
                             ]],
                         ]
    grafo = monta_grafo(lista_de_um_grafo)
    return grafo

#Se estiver executando esse arquivo, roda a função a seguir
#Senão, pula
if __name__ == "__main__":
    um_teste_monta_grafo()