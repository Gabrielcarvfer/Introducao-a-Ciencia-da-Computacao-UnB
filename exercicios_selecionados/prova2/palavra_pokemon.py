entrada = """3 2
char
man
der
pika
char
"""

linhas = entrada.split(sep='\n')

pokemons = ["charmander","pikachu"]

num_entradas = linhas[0].split()
indice_linha = 1
num_entradas = [int(valor) for valor in num_entradas]

dicionario_palavras = {}
for indice_pokemon in range(len(pokemons)):
    dicionario_palavras[pokemons[indice_pokemon]] = {}
    while num_entradas[indice_pokemon] > 0:
        palavra = linhas[indice_linha]
        indice_linha += 1
        dicionario_palavras[pokemons[indice_pokemon]][palavra] = 0
        num_entradas[indice_pokemon] -= 1

sem_vencedor = True
vencedor = ""
while sem_vencedor:
        palavra_nao_dita = ""

        conta_palavras_diferentes_de_0 = 0
        for palavra in dicionario_palavras["charmander"]:
            if dicionario_palavras["charmander"][palavra] == 0:
                palavra_nao_dita = palavra
                break
            conta_palavras_diferentes_de_0 += 1

        if conta_palavras_diferentes_de_0 > 0:
            print("Charmander perdeu")
            sem_vencedor = False
            vencedor = "Pikachu"
            continue
        else:
            #anuncia palavra
            dicionario_palavras["pikachu"][palavra] = -1
            dicionario_palavras["charmander"][palavra] += 1
            pass

        palavra_nao_dita = ""

        conta_palavras_diferentes_de_0 = 0
        for palavra in dicionario_palavras["pikachu"]:
            if dicionario_palavras["pikachu"][palavra] == 0:
                palavra_nao_dita = palavra
                break
            conta_palavras_diferentes_de_0 += 1

        if conta_palavras_diferentes_de_0 > 0:
            print("Pikachu perdeu")
            sem_vencedor = False
            vencedor = "Charmander"
            continue
        else:
            # anuncia palavra
            dicionario_palavras["charmander"][palavra] = -1
            dicionario_palavras["pikachu"][palavra] += 1
            pass
pass
print("Vencedor é o %s" % vencedor)