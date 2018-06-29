
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

drogas_pesadas_plot = {
    "Tamiflu"	      : [],
    "Victoza"	      : [],
    "Ritalina"	      : [],
    "Cianocobalamina" : [],
    "Colecalciferol"  : [],
    "Risperidona"	  : [],
    "Cataflam"	      : [],
    "Tylex"	          : [],
    "Aspirina"	      : [],
    "Ácido Lisérgico" : [],
    "Fenilefrina"     : [],
    "Polaramine"      : [],
    "Triclosan"       : [],
    "Amoxilina"       : [],
    "Fluoxetina"      : [],
    "Ciprofloxacina"  : [],

}

import random
cores = [[random.random(), random.random(), random.random()] for i in range(9)]

import matplotlib
from matplotlib import pyplot as plt
import squarify
        
from matplotlib import patches
        
    
def plot_compostos(lista_compostos):
    fig = plt.gcf()
    ax = fig.add_subplot()

    num_elementos_total = 0
    num_elemento_compostos = {}
    for nome_composto in [x[1] for x in lista_compostos]:
        composto = drogas_pesadas[nome_composto]
        num_elemento_compostos[nome_composto] = 0
        for elemento in composto:
            num_elementos_total += composto[elemento]
            num_elemento_compostos[nome_composto] += composto[elemento]

    num_elemento_compostos_sorted = sorted([[num_elemento_compostos[val],val] for val in num_elemento_compostos], reverse=True)
    rects = squarify.padded_squarify([val for val,key in num_elemento_compostos_sorted], 0, 0, 400, 400)

    for val, key in num_elemento_compostos_sorted:
        pass

    x = [rect['x'] for rect in rects]
    y = [rect['y'] for rect in rects]
    dx = [rect['dx'] for rect in rects]
    dy = [rect['dy'] for rect in rects]
    colors = []
    labels = []

    ax.bar(x, dy, width=dx, bottom=y, color=color, label=labels)
    plt.axis('off')
    plt.show()

#  lista de [numero de vezes que o composto aparece, indice do composto]
lista_compostos = [[2, "Aspirina"],[3,"Fluoxetina"]]


plot_compostos(lista_compostos)
