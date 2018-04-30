#Object-oriented version of the pong game available in http://trevorappleton.blogspot.com.br/2014/04/writing-pong-using-python-and-pygame.html
#Versão orientada a objetos do jogo pong disponível no site acima

#Importação da bibliteca pygame
import pygame, sys
from pygame.locals import *

#Variáveis globais com tamanho da tela
WindowWidth = 400
WindowHeight = 300

#Definição da classe bola
class PongBall():
    #Atributo de classe (disponível para todos os objetos/instâncias da classe)
    LineThickness = 20

    #Método de inicialização (receita de como se criar um objeto, no caso uma bola para Pong
    def __init__(self, X, Y, LineThickness):
        self.LineThickness = LineThickness
        self.rect = pygame.Rect(X, Y, self.LineThickness, self.LineThickness)

    #Método para desenhar a "bola quadrada"
    def drawBall(self, Color, DisplaySurface):
        pygame.draw.rect(DisplaySurface, Color, self.rect)

    #Método para mover a bola para uma posição
    def moveBall(self, ballDirX, ballDirY):
        self.rect.x += ballDirX
        self.rect.y += ballDirY
        return

#Definição da classe paleta (as barrinhas que impedem a bola de bater no canto
class PongPaddle():

    #Método para criar uma paleta
    def __init__(self, LineThickness = 20, PaddleSize = 50, PaddleOffset = 20, InitialPos = (10,10)):
        self.PaddleSize = PaddleSize
        self.PaddleOffset = PaddleOffset
        self.InitialPos = InitialPos
        self.LineThickness = LineThickness
        self.rect = pygame.Rect(InitialPos[0], InitialPos[1], self.LineThickness, self.PaddleSize)

    #Método para desenhar uma paleta
    def drawPaddle(self, WindowHeight, Color, DisplaySurface):
        # Stops paddle moving too low
        if self.rect.bottom > WindowHeight - self.LineThickness:
            self.rect.bottom = WindowHeight - self.LineThickness

        # Stops paddle moving too high
        elif self.rect.top < self.LineThickness:
            self.rect.top = self.LineThickness

        # Draws paddle
        pygame.draw.rect(DisplaySurface, Color, self.rect)

    #Método para paleta controlada por computador
    def artificialIntelligence(self, ball, ballDirX):
       #If ball is moving away from paddle, center bat
       if ballDirX == -1:
           if self.rect.centery < (WindowHeight/2):
               self.rect.y += 1
           elif self.rect.centery > (WindowHeight/2):
               self.rect.y -= 1
       #if ball moving towards bat, track its movement.
       elif ballDirX == 1:
           if self.rect.centery < ball.rect.centery:
               self.rect.y += 1
           else:
               self.rect.y -=1
       return self.rect


#Crio uma classe (conjunto de dados - armazenados em variáveis - e funções altamente relacionadas
# para controlar o jogo
class PongGame():

    #Defino a função de inicialização das instâncias/objetos da classe definida anteriormente 
    #Aqui é feita qualquer configuração que só pode ser feita durante a execução e para cada objeto
    def __init__(self):
        self.FPS = 60
        self.LineThickness = 10
        self.PaddleSize = 50
        self.PaddleOffset = 20
        self.BlackColor = (0, 0, 0)
        self.WhiteColor = (255, 255, 255)
        self.BasicFontSize = 20
        self.BasicFont = None
        self.FpsClock = None
        self.DisplaySurface = None
        self.BasicFont = pygame.font.Font('freesansbold.ttf', self.BasicFontSize)
        self.FpsClock = pygame.time.Clock()
        self.DisplaySurface = pygame.display.set_mode((WindowWidth, WindowHeight))
        pygame.display.set_caption('Pong')

        # Initiate variable and set starting positions
        # any future changes made within rectangles
        self.ballX = WindowWidth / 2 - self.LineThickness / 2
        self.ballY = WindowHeight / 2 - self.LineThickness / 2
        self.playerOnePosition = (WindowHeight - self.PaddleSize) / 2
        self.playerTwoPosition = (WindowHeight - self.PaddleSize) / 2
        self.score = 0

        # Keeps track of ball direction
        self.ballDirX = -1  ## -1 = left 1 = right
        self.ballDirY = -1  ## -1 = up 1 = down

        # Creates Rectangles for ball and paddles.

        self.paddle1 = PongPaddle( LineThickness = self.LineThickness,
                              PaddleSize=self.PaddleSize,
                              PaddleOffset=self.PaddleOffset,
                              InitialPos=(self.PaddleOffset, self.playerOnePosition)
                              )
        self.paddle2 = PongPaddle (LineThickness = self.LineThickness,
                              PaddleSize=self.PaddleSize,
                              PaddleOffset=self.PaddleOffset,
                              InitialPos=(WindowWidth - self.PaddleOffset - self.LineThickness,self.playerTwoPosition)
                              )
        self.ball = PongBall(X=self.ballX, Y=self.ballY, LineThickness=self.LineThickness)

        self.draw()

        pygame.mouse.set_visible(0)  # make cursor invisible

    #Essa função desenha a arena, bola e paletas
    def draw(self):
        # Draws the starting position of the Arena
        self.drawArena()

        self.paddle1.drawPaddle(WindowHeight=WindowHeight,
                           Color=self.WhiteColor,
                           DisplaySurface=self.DisplaySurface
                           )

        self.paddle2.drawPaddle(WindowHeight=WindowHeight,
                           Color=self.WhiteColor,
                           DisplaySurface=self.DisplaySurface)

        self.ball.drawBall(Color=self.WhiteColor,
                           DisplaySurface=self.DisplaySurface)

    #Essa função executa o laço principal do jogo
    def exec(self):
        # No caso, um laço infinito que verifica eventos (movimento do mouse ou +- para controlar velocidade do jogo)
        gameOver = False
        while not gameOver:
            # Laço para verificação de eventos de entrada (mouse, teclado, botões)
            for event in pygame.event.get():
                # click on X button
                if event.type == QUIT:
                    gameOver = True
                    break

                # mouse movement commands
                elif event.type == MOUSEMOTION:
                    mousex, mousey = event.pos
                    self.paddle1.rect.y = mousey

                # keyboard commands
                elif event.type == KEYDOWN:
                    if   event.unicode is '+' and self.FPS < 240:
                        self.FPS += 5
                    elif event.unicode is '-' and self.FPS > 60:
                        self.FPS -= 5
                    elif event.unicode is 'p':
                        gameOver = True
                        break
                    else:
                        pass
            # Se clicar no X ou clicar em 'p', vai entrar nessa condição
            if gameOver:
                # Se entrar nessa condição, volta para o início do while,
                #  que checa a condição e termina a execução
                continue

            # Depois de verificar os eventos, desenha arena, bola e paletas
            self.draw()

            # Movimenta bola
            self.ball.moveBall(self.ballDirX, self.ballDirY)

            # Checa colisão da bola com paredes ou paletas
            self.checkEdgeCollision()

            # Checa se um ponto foi marcado ou se o jogador perde os pontos que tem
            self.checkPointScored()

            # Se houve colisão, muda rumo da bola
            self.ballDirX = self.ballDirX * self.checkHitBall()

            # Paleta 2, do segundo jogador, verifica se movimenta ou não
            self.paddle2.artificialIntelligence(self.ball, self.ballDirX)

            # Imprime a pontuação e velocidade do jogo
            self.displayScore()

            # Atualiza a tela com os elementos desenhados anteriormente
            pygame.display.update()

            # Espera um intervalo de tempo relativo a velocidade do jogo
            self.FpsClock.tick(self.FPS)

            # E executa o laço novamente

    # Imprime a pontuação e velocidade do jogo
    def displayScore(self):
        resultSurf = self.BasicFont.render('FPS = %s    Score = %s' %(self.FPS, self.score), True, self.WhiteColor)
        resultRect = resultSurf.get_rect()
        resultRect.topleft = (WindowWidth - 300, 25)
        self.DisplaySurface.blit(resultSurf, resultRect)

    # Imprime a arena do jogo
    def drawArena(self):
        self.DisplaySurface.fill((0,0,0))

        # Desenha o contorno da arena
        pygame.draw.rect(self.DisplaySurface,
                         self.WhiteColor,
                         ((0,0),(WindowWidth,WindowHeight)),
                         self.LineThickness*2
                         )

        #Desenha a linha central
        pygame.draw.line(self.DisplaySurface,
                         self.WhiteColor,
                         ((WindowWidth/2),0),
                         ((WindowWidth/2),WindowHeight),
                         int(self.LineThickness/4)
                         )

    # Verifica se um ponto foi marcado e atualiza de acordo
    def checkPointScored(self):
        # reset points if left wall is hit
        if self.ball.rect.left == self.LineThickness:
            self.score = 0
        # 1 point for hitting the ball
        elif self.ballDirX == -1 \
                and self.paddle1.rect.right == self.ball.rect.left \
                and self.paddle1.rect.top < self.ball.rect.top \
                and self.paddle1.rect.bottom > self.ball.rect.bottom:
            self.score += 1
        # 5 points for beating the other paddle
        elif self.ball.rect.right == WindowWidth - self.LineThickness:
            self.score += 5
        # if no points scored, return score unchanged
        else:
            pass

    # Verifica colisão com parede e rebate caso necessário
    def checkEdgeCollision(self):
        if self.ball.rect.top == (self.LineThickness) \
                or self.ball.rect.bottom == (WindowHeight - self.LineThickness):
            self.ballDirY = self.ballDirY * -1
        if self.ball.rect.left == (self.LineThickness) \
                or self.ball.rect.right == (WindowWidth - self.LineThickness):
            self.ballDirX = self.ballDirX * -1

    # Verifica colisão com paleta e rebate caso necessário
    def checkHitBall(self):
        if self.ballDirX == -1 \
                and self.paddle1.rect.right >= self.ball.rect.left \
                and self.paddle1.rect.top <= self.ball.rect.top \
                and self.paddle1.rect.bottom >= self.ball.rect.bottom:
            return -1
        elif self.ballDirX == 1 \
                and self.paddle2.rect.left <= self.ball.rect.right \
                and self.paddle2.rect.top <= self.ball.rect.top \
                and self.paddle2.rect.bottom >= self.ball.rect.bottom:
            return -1
        else:
            return 1



# Definição da função principal
def main():
    # Inicializa a biblioteca
    pygame.init()

    # Cria um jogo Pong
    pong = PongGame()

    # Executa o jogo (fica preso no laço até a letra 'p' ser pressionada)
    pong.exec()

    # Finaliza a biblioteca
    pygame.quit()

    # Finaliza a execução
    sys.exit()

main()