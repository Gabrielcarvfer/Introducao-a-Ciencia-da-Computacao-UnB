# Importamos a biblioteca gráfica
import matplotlib.pyplot as pyplot


def plotagem_serie_dados(serie_dados):
    intervalo_impressao = [dado[0] for dado in serie_dados]
    valores_impressao   = [dado[1] for dado in serie_dados]

    fig = pyplot.figure()
    ax = fig.add_subplot(111)

    # Plotamos os valores calculados pela biblioteca matemática
    pyplot.plot(intervalo_impressao, valores_impressao, 'green')

    for a, b in zip(intervalo_impressao, valores_impressao):
            ax.annotate(str(b), xy=(a, b+0.05))

    pyplot.show()


def um_teste_plotagem_serie():
    serie_dados = [ ("11/30/17", 9.78),
                    ("11/29/17",10.03),
                    ("11/28/17",10.14),
                    ("11/27/17",10.18),
                    ("11/24/17",10.34),
                    ("11/22/17",10.12),
                    ("11/21/17",10.26),
                    ("11/20/17",10.04),
                    ("11/17/17",10.05),
                    ("11/16/17",10.10),
                    ("11/15/17", 9.52),
                    ("11/14/17",10.38),
                    ("11/13/17",10.57),
    ]

    plotagem_serie_dados(serie_dados)
    pass

um_teste_plotagem_serie()