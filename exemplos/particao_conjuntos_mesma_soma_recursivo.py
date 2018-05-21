conjunto_elementos = [1,2,3,4,5,6,7]
soma_conjunto = 0
mapa_soma = {}


def monta_mapa():
    global conjunto_elementos, soma_conjunto, mapa_soma
    for elementoX in conjunto_elementos:
        for elementoY in conjunto_elementos:
            mapa_soma[elementoX] = {}
            mapa_soma[elementoY] = {}

    for elementoX in conjunto_elementos:
        soma_conjunto += elementoX
        for elementoY in conjunto_elementos:
            mapa_soma[elementoX][elementoY] = mapa_soma[elementoY][elementoX] = elementoX + elementoY


monta_mapa()


def busca_particao(subconjunto1, subconjunto2, somaParcial1, somaParcial2):

    pass


busca_particao([],[],0,0)
pass
