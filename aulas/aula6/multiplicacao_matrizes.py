def multiplica_matriz(matriz1,matriz2):

    # Verifica se o número de colunas da matriz 2 é igual ao número de linhas da matriz 1
    if len(matriz2) > 0 and len(matriz1) == len(matriz2[0]):


        num_colunas = len(matriz2[0])
        num_linhas = len(matriz1)

        # Matriz resultado terá tamanho min(colunas,linhas)
        produto_matriz = []


        #Seleciona a linha da primeira matriz
        for linha in matriz1:
            # Linha produtos guarda a primeira linha da matriz resultante
            linha_produtos = []

            #E para cada uma das colunas da segunda matriz
            for num_coluna in range(num_colunas):

                soma_coluna = 0
                #Pega a o valor correspondente, multiplica e soma
                for linha_coluna in matriz2:
                    soma_coluna += linha[num_coluna] * linha_coluna[num_coluna]
                linha_produtos += [soma_coluna]

            produto_matriz += [linha_produtos]

        return produto_matriz

    return []


def main():
    matrizA = [[1,0,0],
               [0,1,0],
               [0,0,1]]

    matrizB = [[1,0,0],
               [0,1,0],
               [0,0,1]]

    matrizA1 = [[1, 0, 0],
                [0, 1, 0]]

    matrizB1 = [[1, 0],
                [0, 1],
                [0, 0]]

    produto_matrizes = multiplica_matriz(matrizA, matrizB)
    print(produto_matrizes)

    produto_matrizes = multiplica_matriz(matrizA1, matrizB1)
    print(produto_matrizes)


    return

main()