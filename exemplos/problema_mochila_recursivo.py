# Items cuja soma do volume é maior que o da mochila
#                        Volume e preço
itens_para_selecionar = {0: (1, 10),
                         1: (10, 5),
                         2: (2, 6),
                         3: (3, 1),
                         4: (8, 7),
                         5: (9, 1),
                         6: (1, 2),
                         7: (2, 3),
                         8: (4, 3),
                         9: (4, 8)}

# Uma mochila de tamanho 15, que queremos preencher com os itens de maior valor possível
class Mochila():
    def __init__(self, tamanho=15):
        self.tamanho = tamanho
        self.maiorValor = 0
        self.maiorVolume = 0
        self.itensMaiorValor = []

    # Método (função de uma classe ou objeto) que calcula o volume de uma certa lista de elementos
    @staticmethod
    def calcVolume(elements):
        sum = 0
        for element in elements:
            sum += itens_para_selecionar[element][0]
        return sum

    # Método que insere recursivamente novos elementos na mochila
    def insere_recursivo(self, valorAtual, volumeAtual, itens_selecionados):
        #print("Melhor conjunto com valor %d, volume %d, [%s]" % (valorAtual, volumeAtual, itens_selecionados))

        # Se o volume ocupado for menor ou igual ao tamanho da mochila
        if volumeAtual <= self.tamanho:
            if valorAtual > self.maiorValor:
                # Caso o valor dos itens sem o novo seja maior que o maior conhecido, guarda a lista de itens
                self.maiorValor = valorAtual
                self.maiorVolume = volumeAtual
                self.itensMaiorValor = itens_selecionados

            # Procura outro item para adicionar
            itens_nao_explorados = list(set(itens_para_selecionar.keys()) - set(itens_selecionados))

            for itemRec in itens_nao_explorados:
                if itemRec not in itens_selecionados:
                    self.insere_recursivo(valorAtual+itens_para_selecionar[itemRec][1],
                                          volumeAtual+itens_para_selecionar[itemRec][0],
                                          itens_selecionados + [itemRec])

def main():
    minha_mochila = Mochila()

    for item in itens_para_selecionar.keys():
        minha_mochila.insere_recursivo(itens_para_selecionar[item][1], itens_para_selecionar[item][0], [item])
        #print("%s - Melhor conjunto com valor %d, volume %d, [%s]" % (item, minha_mochila.maiorValor, minha_mochila.maiorVolume, minha_mochila.itensMaiorValor))

    print("Melhor conjunto com valor %d, volume %d, %s" % (
    minha_mochila.maiorValor, minha_mochila.maiorVolume, minha_mochila.itensMaiorValor))

    return 0

main()