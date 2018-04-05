import turtle
import math

segmentSize = 20

colors = ["aquamarine",
          "azure",
          "beige",
          "bisque",
          "black",
          "blue",
          "brown",
          "violet",
          "cyan",
          "firebrick",
          "gold",
          "lavender",
          "lemon chiffon"]

class FunTurtle (turtle.Turtle):

    def drawA(self):
        # Draw
        #  |
        #  |
        #  |
        self.forward(2 * segmentSize)

        # Draw
        #   _
        #  |
        #  |
        #  |
        self.right(90)
        self.forward(segmentSize)

        # Draw
        #   _
        #  | |
        #  | |
        #  |
        self.right(90)
        self.forward(2 * segmentSize)

        # Draw
        #   _
        #  | |
        #  | |
        #  |
        self.right(180)
        self.forward(segmentSize)

        # Draw
        #   _
        #  |_|
        #  | |
        #  |
        self.left(90)
        self.forward(segmentSize)

        # Draw
        #   _
        #  |_|
        #  | |
        #  |
        self.left(90)
        self.forward(segmentSize)

    def drawB(self):
        # Draw
        #  |
        #  |
        #  |
        self.forward(2 * segmentSize)

        # Draw
        #  |
        #  |
        #  |
        self.right(180)
        self.forward(segmentSize)

        # Draw
        #  |_
        #  |
        #  |
        self.left(90)
        self.forward(segmentSize)

        # Draw
        #
        #  |_
        #  | |
        #  |
        self.right(90)
        self.forward(segmentSize)

        # Draw
        #  |_
        #  |_|
        #  |
        self.right(90)
        self.forward(segmentSize)

        # Draw
        #  |_
        #  |_|
        #  |
        self.left(90)

    def drawC(self):
        # Draw
        #  |
        #  |
        self.forward(segmentSize)

        # Draw
        #   _
        #  |
        #  |
        self.right(90)
        self.forward(segmentSize)

        # Draw
        #   _
        #  |
        #  |
        self.right(180)
        self.forward(segmentSize)

        # Draw
        #   _
        #  |
        #  |
        self.left(90)
        self.forward(segmentSize)

        # Draw
        #   _
        #  |_
        #  |
        self.left(90)
        self.forward(segmentSize)

        # Draw
        #   _
        #  |_
        #  |
        self.right(180)
        self.forward(segmentSize)

        # Draw
        #   _
        #  |_
        #  |
        self.left(90)

    def drawD(self):
        # Draw
        #
        #  |
        #  |
        self.forward(segmentSize)

        # Draw
        #   _
        #  |
        #  |
        self.right(90)
        self.forward(segmentSize)

        # Draw
        #   _|
        #  |
        #  |
        self.left(90)
        self.forward(segmentSize)

        # Draw
        #
        #   _|
        #  | |
        #  |
        self.right(180)
        self.forward(2*segmentSize)

        # Draw
        #   _|
        #  |_|
        #  |
        self.right(90)
        self.forward(segmentSize)

        # Draw
        #   _|
        #  |_|
        #  |
        self.left(90)

    def drawE(self):
        # Draw
        #  |
        #  |
        #  |
        self.forward(2*segmentSize)

        # Draw
        #   _
        #  |
        #  |
        #  |
        self.right(90)
        self.forward(segmentSize)

        # Draw
        #   _
        #  |
        #  |
        #  |
        self.right(180)
        self.forward(segmentSize)

        # Draw
        #   _
        #  |
        #  |
        #  |
        self.left(90)
        self.forward(segmentSize)

        # Draw
        #   _
        #  |_
        #  |
        #  |
        self.left(90)
        self.forward(segmentSize)

        # Draw
        #   _
        #  |_
        #  |
        #  |
        self.right(180)
        self.forward(segmentSize)

        # Draw
        #   _
        #  |_
        #  |
        #  |
        self.left(90)
        self.forward(segmentSize)

        # Draw
        #   _
        #  |_
        #  |_
        #  |
        self.left(90)
        self.forward(segmentSize)

        # Draw
        #   _
        #  |_
        #  |_
        #  |
        self.right(180)
        self.forward(segmentSize)

        # Draw
        #   _
        #  |_
        #  |_
        #  |
        self.left(90)

    def drawF(self):
        # Draw
        #  |
        #  |
        #  |
        self.forward(2 * segmentSize)

        # Draw
        #   _
        #  |
        #  |
        #  |
        self.right(90)
        self.forward(segmentSize)

        # Draw
        #   _
        #  |
        #  |
        #  |
        self.right(180)
        self.forward(segmentSize)

        # Draw
        #   _
        #  |
        #  |
        #  |
        self.left(90)
        self.forward(segmentSize)

        # Draw
        #   _
        #  |_
        #  |
        #  |
        self.left(90)
        self.forward(segmentSize)

        # Draw
        #   _
        #  |_
        #  |
        #  |
        self.right(180)
        self.forward(segmentSize)

        # Draw
        #   _
        #  |_
        #  |
        #  |
        self.left(90)
        self.forward(segmentSize)

    def drawG(self):
        # Draw
        #  |
        #  |
        #  |
        self.forward(2 * segmentSize)

        # Draw
        #   _
        #  |
        #  |
        #  |
        self.right(90)
        self.forward(segmentSize)

        # Draw
        #   _
        #  |
        #  |
        #  |
        self.right(180)
        self.forward(segmentSize)

        # Draw
        #   _
        #  |
        #  |
        #  |
        self.left(90)
        self.forward(2*segmentSize)

        # Draw
        #   _
        #  |
        #  |_
        #  |
        self.left(90)
        self.forward(segmentSize)

        # Draw
        #   _
        #  |
        #  |_|
        #  |
        self.left(90)
        self.forward(segmentSize)

        # Draw
        #   _
        #  |
        #  |_|
        #  |
        self.left(180)
        self.forward(segmentSize)

        # Draw
        #   _
        #  |
        #  |_|
        #  |
        self.right(90)
        self.forward(segmentSize)

        # Draw
        #   _
        #  |
        #  |_|
        #  |
        self.left(90)

    def drawH(self):
        # Draw
        #  |
        #  |
        #  |
        self.forward(2 * segmentSize)

        # Draw
        #  |
        #  |
        #  |
        self.right(180)
        self.forward(segmentSize)

        # Draw
        #  |_
        #  |
        #  |
        self.left(90)
        self.forward(segmentSize)

        # Draw
        #  |_|
        #  |
        #  |
        self.left(90)
        self.forward(segmentSize)

        # Draw
        #  |_|
        #  | |
        #  |
        self.left(180)
        self.forward(2*segmentSize)

        # Draw
        #  |_|
        #  | |
        #  |
        self.left(180)
        self.forward(segmentSize)

        # Draw
        #  |_|
        #  | |
        #  |
        self.left(90)
        self.forward(segmentSize)

        # Draw
        #  |_|
        #  | |
        #  |
        self.left(90)
        self.forward(segmentSize)

    def drawI(self):
        # Draw
        #
        #
        #   __
        #  |
        self.right(90)
        self.forward(segmentSize)

        # Draw
        #
        #
        #   __
        #  |
        self.right(180)
        self.forward(segmentSize/2)

        # Draw
        #
        #    |
        #   _|_
        #  |
        self.right(90)
        self.forward(2*segmentSize)

        # Draw
        #   _
        #    |
        #   _|_
        #  |
        self.left(90)
        self.forward(segmentSize/2)

        # Draw
        #   _ _
        #    |
        #   _|_
        #  |
        self.left(180)
        self.forward(segmentSize)

        # Draw
        #   _ _
        #    |
        #   _|_
        #  |
        self.left(180)
        self.forward(segmentSize/2)

        # Draw
        #   _ _
        #    |
        #   _|_
        #  |
        self.left(90)
        self.forward(2*segmentSize)

        # Draw
        #   _ _
        #    |
        #   _|_
        #  |
        self.right(90)
        self.forward(segmentSize/2)

        # Draw
        #   _ _
        #    |
        #   _|_
        #  |
        self.left(90)

    def drawJ(self):
        # Draw
        #
        #   _
        #  |
        self.right(90)
        self.forward(segmentSize)

        # Draw
        #    |
        #   _|
        #  |
        self.left(90)
        self.forward(2 * segmentSize)

        # Draw
        #    |
        #   _|
        #  |
        self.left(180)
        self.forward(2 * segmentSize)

        # Draw
        #    |
        #   _|
        #  |
        self.right(90)
        self.forward(segmentSize)

        # Draw
        #    |
        #   _|
        #  |
        self.right(90)
        self.forward(segmentSize)

        # Draw
        #    |
        #   _|
        #  |
        self.right(180)
        self.forward(segmentSize)

    def drawK(self):
        pass
    def drawL(self):
        # Draw
        #  |
        #  |
        #  |
        self.forward(2 * segmentSize)

        # Draw
        #  |
        #  |
        #  |
        self.right(180)
        self.forward(2 * segmentSize)

        # Draw
        #  |
        #  |_
        #  |
        self.left(90)
        self.forward(segmentSize)

        # Draw
        #  |
        #  |_
        #  |
        self.left(180)
        self.forward(segmentSize)

        # Draw
        #  |
        #  |_
        #  |
        self.left(90)

    def drawM(self):
        pass
    def drawN(self):
        pass
    def drawO(self):
        # Draw
        #
        #  |
        #  |
        self.forward(segmentSize)

        # Draw
        #   _
        #  |
        #  |
        self.right(90)
        self.forward(segmentSize)

        # Draw
        #   _
        #  | |
        #  |
        self.right(90)
        self.forward(segmentSize)

        # Draw
        #   _
        #  |_|
        #  |
        self.right(90)
        self.forward(segmentSize)

        # Draw
        #   _
        #  |_|
        #  |
        self.left(90)

    def drawP(self):
        # Draw
        #  |
        #  |
        #  |
        self.forward(2 * segmentSize)

        # Draw
        #   _
        #  |
        #  |
        #  |
        self.right(90)
        self.forward(segmentSize)

        # Draw
        #   _
        #  | |
        #  |
        #  |
        self.right(90)
        self.forward(segmentSize)

        # Draw
        #   _
        #  |_|
        #  |
        #  |
        self.right(90)
        self.forward(segmentSize)

        # Draw
        #   _
        #  |_|
        #  |
        #  |
        self.left(90)
        self.forward(segmentSize)

    def drawQ(self):
        pass
    def drawR(self):
        # Draw
        #  |
        #  |
        #  |
        self.forward(2*segmentSize)

        # Draw
        #   _
        #  |
        #  |
        #  |
        self.right(90)
        self.forward(segmentSize)

        # Draw
        #   _
        #  | |
        #  |
        #  |
        self.right(90)
        self.forward(segmentSize)

        # Draw
        #   _
        #  |_|
        #  |
        #  |
        self.right(90)
        self.forward(segmentSize)

        # Draw
        #   _
        #  |_|
        #  |\
        #  |
        self.left(45+90)
        self.forward(segmentSize*math.sqrt(2))

        # Draw
        #   _
        #  |_|
        #  |\
        #  |
        self.left(180)
        self.forward(segmentSize*math.sqrt(2))

        # Draw
        #   _
        #  |_|
        #  |\
        #  |
        self.left(45+90)
        self.forward(segmentSize)

    def drawS(self):
        pass
    def drawT(self):
        pass
    def drawU(self):
        pass
    def drawV(self):
        pass
    def drawW(self):
        pass
    def drawX(self):
        pass
    def drawY(self):
        pass
    def drawZ(self):
        pass
    def draw0(self):
        # Draw
        #  |
        #  |
        #  |
        self.forward(2*segmentSize)

        # Draw
        #   _
        #  |
        #  |
        #  |
        self.right(90)
        self.forward(segmentSize)

        # Draw
        #   _
        #  | |
        #  | |
        #  |
        self.right(90)
        self.forward(2*segmentSize)

        # Draw
        #   _
        #  | |
        #  |_|
        #  |
        self.right(90)
        self.forward(segmentSize)

        # Draw
        #   _
        #  | |
        #  |_|
        #  |
        self.left(90)

    def draw1(self):
        pass
    def draw2(self):
        pass
    def draw3(self):
        pass
    def draw4(self):
        pass
    def draw5(self):
        pass
    def draw6(self):
        pass
    def draw7(self):
        pass
    def draw8(self):
        pass
    def draw9(self):
        pass


    drawSymbols = {'A': drawA,
                   'B': drawB,
                   'C': drawC,
                   'D': drawD,
                   'E': drawE,
                   'F': drawF,
                   'G': drawG,
                   'H': drawH,
                   'I': drawI,
                   'J': drawJ,
                   'K': drawK,
                   'L': drawL,
                   'M': drawM,
                   'N': drawN,
                   'O': drawO,
                   'P': drawP,
                   'Q': drawQ,
                   'R': drawR,
                   'S': drawS,
                   'T': drawT,
                   'U': drawU,
                   'V': drawV,
                   'W': drawW,
                   'X': drawX,
                   'Y': drawY,
                   'Z': drawZ,
                   '0': draw0,
                   '1': draw1,
                   '2': draw2,
                   '3': draw3,
                   '4': draw4,
                   '5': draw5,
                   '6': draw6,
                   '7': draw7,
                   '8': draw8,
                   '9': draw9,}

    def draw(self, character):
        self.left(90)
        self.forward(segmentSize)
        self.color("green")
        self.pensize(3)

        self.drawSymbols[character](self)

        self.color("black")
        self.pensize(1)
        self.forward(segmentSize)
        self.left(90)
        self.forward(2*segmentSize)


    def drawString(self, string):
        for character in string:
            self.draw(character)

    def drawCircle(self, numberOfColors, radius):
        for i in range(45):
            self.pensize(3)
            self.color(colors[i % numberOfColors % len(colors)])
            self.forward(radius)
            self.left(8)