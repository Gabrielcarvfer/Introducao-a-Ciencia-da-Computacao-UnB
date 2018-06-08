drogas_pesadas = {
    "Tamiflu"	      : {'C': 16, 'H': 28, 'O' :  4, 'N' :  2, 'Cl':  0, 'Co':  0, 'P': 0, 'S': 0, 'F' :  0, },
    "Victoza"	      : {'C':172, 'H':265, 'O' : 51, 'N' : 43, 'Cl':  0, 'Co':  0, 'P': 0, 'S': 0, 'F' :  0, },
    "Ritalina"	      : {'C': 14, 'H': 19, 'O' :  2, 'N' :  1, 'Cl':  0, 'Co':  0, 'P': 0, 'S': 0, 'F' :  0, },
    "Cianocobalamina" : {'C': 63, 'H': 88, 'O' : 14, 'N' : 14, 'Cl':  0, 'Co':  1, 'P': 1, 'S': 0, 'F' :  0, },
    "Colecalciferol"  : {'C': 27, 'H': 44, 'O' :  1, 'N' :  0, 'Cl':  0, 'Co':  0, 'P': 0, 'S': 0, 'F' :  0, },
    "Risperidona"	  : {'C': 23, 'H': 27, 'O' :  2, 'N' :  4, 'Cl':  0, 'Co':  0, 'P': 0, 'S': 0, 'F' :  1, },
    "Cataflam"	      : {'C': 14, 'H': 11, 'O' :  2, 'N' :  1, 'Cl':  2, 'Co':  0, 'P': 0, 'S': 0, 'F' :  0, },
    "Tylex"	          : {'C': 18, 'H': 21, 'O' :  3, 'N' :  1, 'Cl':  0, 'Co':  0, 'P': 0, 'S': 0, 'F' :  0, },
    "Aspirina"	      : {'C':  9, 'H':  8, 'O' :  4, 'N' :  0, 'Cl':  0, 'Co':  0, 'P': 0, 'S': 0, 'F' :  0, },
    "Ácido Lisérgico" : {'C': 20, 'H': 25, 'O' :  1, 'N' :  3, 'Cl':  0, 'Co':  0, 'P': 0, 'S': 0, 'F' :  0, },
    "Fenilefrina"     : {'C':  9, 'H': 13, 'O' :  2, 'N' :  1, 'Cl':  0, 'Co':  0, 'P': 0, 'S': 0, 'F' :  0, },
    "Polaramine"      : {'C': 16, 'H': 19, 'O' :  0, 'N' :  2, 'Cl':  1, 'Co':  0, 'P': 0, 'S': 0, 'F' :  0, },
    "Triclosan"       : {'C': 12, 'H':  7, 'O' :  2, 'N' :  0, 'Cl':  3, 'Co':  0, 'P': 0, 'S': 0, 'F' :  0, },
    "Amoxilina"       : {'C': 16, 'H': 19, 'O' :  5, 'N' :  3, 'Cl':  0, 'Co':  0, 'P': 0, 'S': 0, 'F' :  0, },
    "Fluoxetina"      : {'C': 17, 'H': 18, 'O' :  1, 'N' :  1, 'Cl':  0, 'Co':  0, 'P': 0, 'S': 0, 'F' :  3, },
    "Ciprofloxacina"  : {'C': 17, 'H': 18, 'O' :  3, 'N' :  3, 'Cl':  0, 'Co':  0, 'P': 0, 'S': 0, 'F' :  1, },
}

import random

def gera_lista():
    lista_drogas = {}
    drogas_na_lista = {}
    for i in range(20):
        j = random.randint(0,200)
        indice_droga = j % len(drogas_pesadas)
        nome_droga_pesada = list(drogas_pesadas.keys())[indice_droga]

        if nome_droga_pesada not in drogas_na_lista.keys():
            drogas_na_lista[nome_droga_pesada] = 1
        else:
            drogas_na_lista[nome_droga_pesada] += 1


        for key in drogas_pesadas[nome_droga_pesada]:
            if key not in lista_drogas.keys():
                lista_drogas[key] = drogas_pesadas[nome_droga_pesada][key]
            else:
                lista_drogas[key] += drogas_pesadas[nome_droga_pesada][key]

    print(lista_drogas)
    print(drogas_na_lista)

gera_lista()