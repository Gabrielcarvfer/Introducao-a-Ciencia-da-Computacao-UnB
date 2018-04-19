import turtle


def cria_janela(cor, titulo):
    janela = turtle.Screen()
    janela.bgcolor(cor)
    janela.title(titulo)
    return janela


def cria_tartaruga(cor, tamanho):
    bicho = turtle.Turtle()
    bicho.color(cor)
    bicho.pensize(tamanho)
    return bicho


def koch(bicho, ordem, tamanho):
    if ordem == 0:
        bicho.forward(tamanho)
    else:
        for angulo in [60, -120, 60, 0]:
            koch(bicho, ordem - 1, tamanho / 3)
            bicho.left(angulo)


tela = cria_janela("lightgreen", "Funções com tartarugas")
jarbas = cria_tartaruga("blue", 3)


def moveCanetaEsquerda(bicho):
    bicho.penup()
    bicho.backward(300)
    bicho.pendown()

def koch1(bicho, ordem):
    koch(bicho, ordem, 400)

def koch2(bicho, ordem, lados):
    for _ in range(lados):
        koch(bicho, ordem, 400)
        bicho.right(360/lados)

def quadrado(bicho, tamanho):
    for _ in range(4):
        bicho.forward(tamanho)
        bicho.right(90)


def quadrado_circular_diminuindo(bicho,tamanho):
    if tamanho < 12:
        return

    for angulo in [91,91,91,91]:
        bicho.forward(tamanho)
        bicho.right(angulo)
        tamanho -=10
    quadrado_circular_diminuindo(bicho, tamanho)

def quadrado_circular(bicho,tamanho, graus):
    if graus > 0:
        quadrado(bicho, tamanho)
        bicho.right(10)
        quadrado_circular(bicho,tamanho, graus-10)

#moveCanetaEsquerda(jarbas)
#koch1()
#koch2()


#quadrado_circular_diminuindo(jarbas,500)
quadrado_circular(jarbas,100,100)

pass
