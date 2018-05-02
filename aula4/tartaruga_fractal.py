


def cria_janela(cor, titulo):
    import turtle
    janela = turtle.Screen()
    janela.bgcolor(cor)
    janela.title(titulo)
    janela._RUNNING = True
    return janela


def cria_tartaruga(cor, tamanho):
    import turtle
    bicho = turtle.Turtle()
    bicho.color(cor)
    bicho.pensize(tamanho)
    bicho.shape("turtle")
    bicho.penup()
    bicho.setposition(-300, 200)
    bicho.pendown()
    bicho.speed("fast")
    return bicho


def koch(bicho, ordem, tamanho):
    if ordem == 0:
        bicho.forward(tamanho)
    else:
        for angulo in [60, -120, 60, 0]:
            koch(bicho, ordem - 1, tamanho / 3)
            bicho.left(angulo)


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


def imprime_opcoes():
    print("Digite uma opção para a tartaruga fractal")
    print("0 - Sair da tartaruga fractal")
    print("1 - Koch 1")
    print("2 - Koch 2")
    print("3 - Quadrado")
    print("4 - Quadrado diminuindo")
    print("5 - Quadrado diminuindo enquanto gira")


import gvar


def main():
    global turtleScreen


    if gvar.turtleScreen == 0:
        gvar.turtleScreen = cria_janela("white", "Funções com tartarugas")

    while True:
        imprime_opcoes()
        opcao = int(input())


        jarbas = cria_tartaruga("green", 3)

        if opcao not in [0, 1,2,3,4,5]:
            "Opcao da tartaruga fractal não é válida"
            continue
        if opcao == 0:
            break
        if opcao == 1:
            koch1(jarbas, 2)
        elif opcao == 2:
            koch2(jarbas, 4, 50)
        elif opcao == 3:
            quadrado(jarbas, 50)
        elif opcao == 4:
            quadrado_circular(jarbas, 400, 5)
        elif opcao  == 5:
            quadrado_circular_diminuindo(jarbas,400)
        else:
            pass

        gvar.turtleScreen.clearscreen()

    return