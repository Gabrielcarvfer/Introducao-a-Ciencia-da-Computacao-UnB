from copy import deepcopy


def resolve_problema_mochila(mistura_farmacos):
    # Utiliza memoização para evitar
    # reprocessar combinações inviáveis
    memoria_mochilas_nao_solucao = {}
    def adiciona_item_mochila(item, mochila, mochila_moleculas):
        # Se esta molécula não estiver na mochila, adiciona
        if item not in mochila_moleculas:
            mochila_moleculas[item] = 0
        mochila_moleculas[item] += 1

        # Transforma dicionário em uma tupla para servir
        # de chave para o dicionário de não soluções
        key = tuple(sorted(mochila_moleculas.items()))

        # Verifica se a mochila já está no dicionário de não soluções
        if key in memoria_mochilas_nao_solucao:
            # Caso esteja, interrompe execução
            return None, None

        # Caso não esteja, processa
        for (nome_atomo, numero_atomos) in dicio_quimicos[item].items():
            if nome_atomo not in mochila:
                mochila[nome_atomo] = 0
            mochila[nome_atomo] += numero_atomos
            # Caso o número de átomos na mochila ultrapasse os da mistura,
            # interrompe execução e marca como não solução
            if mochila[nome_atomo] > mistura_farmacos[nome_atomo]:
                memoria_mochilas_nao_solucao[key] = False
                return None, None

        # Verifica se o número de átomos já na mochila batem com os da mistura
        resultado_final = True
        for (nome_atomo, numero_atomos) in mistura_farmacos.items():
            if nome_atomo not in mochila:
                resultado_final = False
                break
            if mochila[nome_atomo] != numero_atomos:
                resultado_final = False
                break
        if resultado_final:
            return mochila, mochila_moleculas
        else:
            # Caso não seja solução, adiciona a lista de não soluções
            memoria_mochilas_nao_solucao[key] = False

        # Tenta adicionar todos os químicos
        for farmaco in dicio_quimicos:
            mochila_ret = adiciona_item_mochila(farmaco, deepcopy(mochila), deepcopy(mochila_moleculas))
            if mochila_ret[0] == None:
                continue
            return mochila_ret

        # Caso não haja nenhuma solução viável
        return None, None

    for farmaco in dicio_quimicos:
        mochila_resultado = adiciona_item_mochila(farmaco, {}, {})
        if mochila_resultado[0] is not None:
            return mochila_resultado


import csv

with open("tabela_consulta_quimicos.csv", "r") as f:
    leitor = csv.DictReader(f)
    dicio_quimicos = {}
    for entrada in leitor:
        nome_composto = entrada[leitor.fieldnames[0]].strip()
        dicio_quimicos[nome_composto] = entrada
        for chave in list(dicio_quimicos[nome_composto].keys()):
            # Tenta transformar valores de string para numero
            try:
                dicio_quimicos[nome_composto][chave] = int(dicio_quimicos[nome_composto][chave])
            except:
                pass
            # Corta espaços em brancos dos nomes dos átomos
            dicio_quimicos[nome_composto][chave.strip()] = dicio_quimicos[nome_composto][chave]
            del dicio_quimicos[nome_composto][chave]
        del dicio_quimicos[nome_composto]["Nome"]
    del leitor, entrada, chave

with open("tabela_conjunto_elementos.csv", "r") as f:
    leitor = csv.DictReader(f)
    for mistura_farmacos_reader in leitor:
        mistura_farmacos = {}
        for (key, value) in mistura_farmacos_reader.items():
            mistura_farmacos[key.strip()] = int(value)
        del mistura_farmacos_reader, key, value
        # Heuristica: elimina quimicos que contém
        # um átomo não presente em dicio_farmacos
        dicio_quimicos_bak = deepcopy(dicio_quimicos)
        for atomo in mistura_farmacos:
            for farmaco in dicio_quimicos:
                if mistura_farmacos[atomo] == 0 and dicio_quimicos[farmaco][atomo] != 0:
                    del dicio_quimicos[farmaco]
                    break
        solucao = resolve_problema_mochila(mistura_farmacos)
        print(solucao)
        dicio_quimicos = dicio_quimicos_bak
        exit(0) # interrompe após primeira solução

