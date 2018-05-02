from turtleFun.FunTurtle import FunTurtle
import turtle

import gvar


def main():
    global turtleScreen


    if gvar.turtleScreen == 0:
        gvar.turtleScreen = turtle.Screen()

    michelangelo = FunTurtle()

    michelangelo.shape("turtle")

    michelangelo.penup()
    michelangelo.setposition(-300, 0)
    michelangelo.pendown()


    michelangelo.speed("fast")

    print("Digite uma frase para a tartaruga escriba")
    string = input()

    michelangelo.drawString(string)

    gvar.turtleScreen.clearscreen()

    return

#main()
