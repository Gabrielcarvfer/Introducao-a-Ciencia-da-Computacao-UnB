import exemplos.grafos.monta_grafo as mg


def grafo_busca_largura(grafo, no_inicio, no_destino):
    fila = [grafo[no_inicio]]
    fila[0].dist = 0
    print("Fila: ", [vizinho.indice for vizinho in fila])

    while len(fila) > 0:
        # Caso o nó explorado seja o destino, termine a busca
        if fila[0] == no_destino:
            break;

        #Caso não seja o nó destino, continue a busca
        novo_caminho = list(fila[0].caminho_da_raiz)
        novo_caminho.append(fila[0].indice)
        for k in fila[0].vizinhos.keys():
            if grafo[k].visitado == mg.EstadoGrafo.NAO:
                grafo[k].visitado = mg.EstadoGrafo.PRIMEIRA_VEZ
                grafo[k].dist = fila[0].dist + 1
                grafo[k].caminho_da_raiz = novo_caminho
                fila.append(grafo[k])


        fila[0].visitado = mg.EstadoGrafo.SIM
        fila.pop(0)
        print("Fila: ", [vizinho.indice for vizinho in fila])


def main():
    ORIGEM = 1
    DESTINO = 5
    nos = mg.um_teste_monta_grafo()
    grafo_busca_largura(nos, ORIGEM, DESTINO)

    if nos[DESTINO].dist != mg.INF:
        print("O nó", nos[DESTINO].indice,"é alcançável partindo do nó", nos[ORIGEM].indice,
              "com distância", nos[DESTINO].dist, "passando pelos nós", nos[DESTINO].caminho_da_raiz)
    else:
        print("O nó", nos[DESTINO].indice, "não é alcançável partindo do nó", nos[ORIGEM].indice)
    pass


#Se estiver executando esse arquivo, roda a função a seguir
#Senão, pula
if __name__ == "__main__":
    main()