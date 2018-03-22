import turtle
from FunTurtle import FunTurtle


def main():
    window = turtle.Screen()

    window.screensize(2000, 1000)

    michelangelo = FunTurtle()

    michelangelo.shape("turtle")

    michelangelo.penup()
    michelangelo.setposition(-300, 0)
    michelangelo.pendown()


    michelangelo.speed("slowest")

    michelangelo.drawString("ABCDEFGHIJLOPR0")

    michelangelo.drawCircle(4, 20)

    window.mainloop()


main()
