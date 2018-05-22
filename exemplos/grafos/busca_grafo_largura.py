import random
INF = 99999999999999999999999999

NAO = 0
PRIMEIRA_VEZ = 1
SIM = 2

class Grafo():
    def __init__(self, indice = 0):
        self.indice = indice
        self.dist = INF
        self.vizinhos = []
        self.visitado = NAO
        self.caminho_da_raiz = []

nos = [Grafo(x) for x in range(10)]

def get_limites(size):
    limite_inferior = random.randrange(0, size-1)
    limite_superior = random.randrange(1, size)
    return limite_inferior, limite_superior

for j in range(len(nos)):
    limite_inferior, limite_superior = get_limites(len(nos))
    for i in range(limite_inferior, limite_superior):
        nos[j].vizinhos.append(nos[i])
        nos[i].vizinhos.append(nos[j])


def grafo_busca_largura(no_inicio, no_destino):
    fila = [no_inicio]
    fila[0].dist = 0

    while len(fila) > 0:
        # Caso o nó explorado seja o destino, termine a busca
        if fila[0] == no_destino:
            break;

        #Caso não seja o nó destino, continue a busca
        num_vizinhos = len(fila[0].vizinhos)
        novo_caminho = list(fila[0].caminho_da_raiz)
        novo_caminho.append(fila[0].indice)
        for k in range(num_vizinhos):
            if fila[0].vizinhos[k].visitado == NAO:
                fila[0].vizinhos[k].visitado = PRIMEIRA_VEZ
                fila[0].vizinhos[k].dist = fila[0].dist + 1
                fila[0].vizinhos[k].caminho_da_raiz = novo_caminho
                fila.append(fila[0].vizinhos[k])


        fila[0].visitado = SIM
        fila.pop(0)
        print([vizinho.indice for vizinho in fila])


def main():
    ORIGEM = 0
    DESTINO = 8
    grafo_busca_largura(nos[ORIGEM], nos[DESTINO])

    if nos[DESTINO].dist != INF:
        print("O nó", nos[DESTINO].indice,"é alcançável partindo do nó", nos[ORIGEM].indice,
              "com distância", nos[DESTINO].dist, "passando pelos nós", nos[DESTINO].caminho_da_raiz)
    else:
        print("O nó", nos[DESTINO].indice, "não é alcançável partindo do nó", nos[ORIGEM].indice)
    pass

main()