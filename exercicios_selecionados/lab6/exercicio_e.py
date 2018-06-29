
tamanho = int(input())

matriz = []

#Lemos varias entradas e guardamos numa lista para as linhas
for indice in range(tamanho):
    matriz.append(input().split())

#Para simular um ciclo, bastam 2 laços, um para linhas e outro para colunas
#Começamos de baixo para cima, já que as coisas estão caindo, e coluna a coluna
for coluna in range(tamanho):
    for linha in range(tamanho-1,0,-1):
        caractere_atual = matriz[linha][coluna]

        #Se caractere atual, for imóvel, o imediatamente acima não tem como descer
        if caractere_atual == 'x':
            continue

        #Se for 'o', e estiver no chão, cai para fora do mapa
        if linha == tamanho -1 and caractere_atual == 'o':
            matriz[linha][coluna] = '.'

        #Se o atual não for imóvel, verifica se o acima é um o
        caractere_acima = matriz[linha-1][coluna]

        if caractere_acima == 'o':
            #Caso seja, o caractere atual é substituido pelo 'o' e o acima por '.'
            matriz[linha][coluna] = 'o'
            matriz[linha-1][coluna] = '.'

#Imprime solução
for linha in matriz:
    print(linha)


