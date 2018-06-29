def simplifica_recursivo(produtos_a_serem_somados):

    # Para cada produto
    itens_removidos = 0
    for produto_i in range(len(produtos_a_serem_somados)):
        produto = produtos_a_serem_somados[produto_i-itens_removidos]
        #Se alguma condição anular o produto inteiro, marcamos com a flag
        fim_de_estrada_para_produto = False

        #1º passo - Verifica se existem um elemento e o mesmo elemento negado, se sim, zera produto
        elementos_conhecidos = [[],[]]
        for elemento in range(len(produto)):
            if len(produto[elemento]) == 1 and "N"+produto[elemento] not in elementos_conhecidos[1]:
                elementos_conhecidos[0] += [produto[elemento]]
            elif len(produto[elemento]) == 2 and produto[elemento][1] not in elementos_conhecidos[0]:
                elementos_conhecidos[1] += [produto[elemento]]
            else:
                #achamos um produto de um elemento e seu inverso, que resultam em produto 0
                fim_de_estrada_para_produto = True
                break

        #Se tivermos achado um produto de inversos, remove o produto da lista e passa para proximo produto
        if fim_de_estrada_para_produto:
            produtos_a_serem_somados.pop(produto_i)
            itens_removidos += 1
            continue


        # 2º passo - Verifica se existem elementos repetidos no produto, se sim, remove
        elementos_conhecidos = {}
        for elemento in range(len(produto)):
            if produto[elemento] not in elementos_conhecidos:
                elementos_conhecidos[produto[elemento]] = [elemento]
            else:
                elementos_conhecidos[produto[elemento]] += [elemento]

        for elemento in elementos_conhecidos.keys():
                while len(elementos_conhecidos[elemento])>1:
                    produto.pop(elementos_conhecidos[elemento][-1])
                    elementos_conhecidos[elemento].pop(-1)

    # 3º passo - Procurar fatores comuns entre diferentes produtos e uní-los

    pass


    booleano_simplificado = ""
    return booleano_simplificado


def minimiza_logica_booleana(soma_de_produtos_str):
    produtos_a_serem_somados_str = soma_de_produtos_str.split(sep='+')
    produtos_a_serem_somados = []

    #Transforma string em lista (produtos a somar) de listas (produtos)
    for produto_str in produtos_a_serem_somados_str:
        produtos_a_serem_somados.append(produto_str.split(sep='*'))
        pass

    #Simplifica recursivamente
    retorno = simplifica_recursivo(produtos_a_serem_somados)

    return retorno





# Se estiver executando esse arquivo, roda a função a seguir
# Senão, pula
if __name__ == "__main__":

    def main():
        entrada = "A*NB+NA*A*A*B+A*A*B"
        print(minimiza_logica_booleana(entrada))


    main()
