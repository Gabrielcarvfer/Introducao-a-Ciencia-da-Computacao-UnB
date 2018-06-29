def main():
    #Lê numero de elementos
    num_elementos = int(input())

    #Lê elementos
    lista_elementos = input().split()
    copia_lista = list(lista_elementos)

    #Checa para ver se o tamanho bate
    if len(lista_elementos) != num_elementos:
        return()

    #Executa 5 comandos
    for iteracao in range(5):

        #Lê comando a ser executado
        comando = input().split()

        #Verifica se tem tamanho 3
        if len(comando) != 3:
            return()

        #Traduz comando para variáveis descritas na lista
        B,D,Q = comando
        Q = int(Q)

        #Verifica posição da letra com valor igual ao lido em B
        try:
            #Quando elemento não existe, index causa um erro
            #Para não interromper a execução, capturamos o erro com try-except
            B_posicao = lista_elementos.index(B)
        except:
            #Elemento não existe na lista
            return()

        #D guarda a direção (esquerda ou direta)
        #Em termos de lista, devemos colocar a letra B (atualmente em B_posicao) em B+-Q
        # +- são, respectivamente, Direita e Esquerda

        posicao_alvo = B_posicao
        if D == 'E':
            posicao_alvo = (posicao_alvo - Q) % num_elementos
        if D == 'D':
            posicao_alvo = (posicao_alvo + Q) % num_elementos

        #O módulo é utilizado porque é como se o elemento desse a
        # volta de um lado para o outro caso esteja nos cantos

        #Agora devemos remover o elemento B da posição B_posicao da lista, e recolocar em posicao_alvo
        lista_elementos.pop(B_posicao)
        lista_elementos.insert(posicao_alvo, str(B))

        #print(lista_elementos)

    #Depois dos 5 comandos, verifica quantas letras mudaram
    elementos_fora_do_lugar = 0
    for indice_elemento in range(num_elementos):
        if lista_elementos[indice_elemento] != copia_lista[indice_elemento]:
            elementos_fora_do_lugar += 1

    #Imprime numero de letras fora do lugar
    print(elementos_fora_do_lugar)

main()