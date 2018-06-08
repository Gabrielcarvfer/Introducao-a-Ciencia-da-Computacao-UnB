
tabela_verdade = []
import random
for i in range(256):
    nova_linha = list("{0:{fill}8b}".format(i, fill='0'))
    for saida in range(3):
        nova_linha += [str(random.randint(0,1))]
    tabela_verdade.append(nova_linha)

for i in range(256):
    print("".join(tabela_verdade[i]))