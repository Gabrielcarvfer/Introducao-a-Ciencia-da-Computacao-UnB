import exemplos.joguinhos.pong_refactor as Pong
import exemplos.matematicos.tangente_recursivo as Tan
import exemplos.tartarugas.main as Tar_Esc
import aulas.aula4.tartaruga_fractal as Tar_Frac


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
    opcao = PONG
    while opcao != SAIR:
        imprime_opcoes()

        opcao = int(input())

        if opcao == SAIR:
            continue
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