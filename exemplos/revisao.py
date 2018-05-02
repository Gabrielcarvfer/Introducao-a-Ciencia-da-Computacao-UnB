import exemplos.pong_refactor as Pong
import exemplos.tangente_recursivo as Tan
import turtleFun.main as Tar_Esc
import aula4.tartaruga_fractal as Tar_Frac


SAIR = 0
PONG = 1
TAN  = 2
TAR_ESC = 3
TAR_FRAC = 4


def imprime_opcoes():
    print("Digite uma opção (número) e aperte enter")
    print("%d - Jogo Pong" % PONG)
    print("%d - Tangente Recursivo" % TAN)
    print("%d - Tartaruga Escriba" % TAR_ESC)
    print("%d - Tartagura Fractal" % TAR_FRAC)
    print()


def main():
    opcao = SAIR
    while True:
        imprime_opcoes()

        opcao = int(input())

        if opcao == SAIR:
            break
        elif opcao == PONG:
            Pong.main()
        elif opcao == TAN:
            Tan.main()
        elif opcao == TAR_ESC:
            Tar_Esc.main()
        elif opcao == TAR_FRAC:
            Tar_Frac.main()
        else:
            print("Tente novamente")

main()