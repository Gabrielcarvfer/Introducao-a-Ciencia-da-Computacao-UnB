estados = ["trabalhando", "dormindo", "jogando", "cansado"]
estadoAtual = ""
paraEsseNegocio = False #variavel de condição para indicar se o programa deve parar ou não

#estas são funções, são usadas para separar do programa principal
# atividades peculiarmente repetitivas

def canse():
    # o comando seguinte indica que a variável está definida fora da função
    global estadoAtual
    print("chega de trabalho por hoje")
    estadoAtual = estados[3]

def trabalhe():
    global estadoAtual
    print("trabalhando")
    estadoAtual = estados[0]

def acorde():
    global estadoAtual
    print("acordando")
    estadoAtual = estados[2] # jogando
    print("hora de jogar")

def durma():
    global estadoAtual
    print("boa noite")
    estadoAtual = estados[1] # dormindo


# puramente opcional, mas é um caso real de uso, portanto exemplos
#  esse pedaço de código será executado caso digite Ctrl+C (chamado de sinal de interrupção, SIGINT)
#  alterando o valor da variável "paraEsseNegocio"
import signal

def tratamento_de_interrupcao_pelo_teclado(signum, frame):
    global paraEsseNegocio
    paraEsseNegocio = True

signal.signal(signal.SIGINT, tratamento_de_interrupcao_pelo_teclado)



#esse é o laço principal, que repete e repete
#usando funções para deixar mais simples, o significado dele é mais legivel
while True:
    if estadoAtual == "trabalhando":
        canse()
    elif estadoAtual == "dormindo":
        acorde()
    elif estadoAtual == "jogando":
        trabalhe()
    elif estadoAtual == "cansado":
        durma()
    else:
        # o laço seguinte é executado até o usuário entrar um comando válido
        while True:
            #já que estamos aqui, vamos perguntar para o usuário onde quer começar
            print("Olá, o que gostaria de fazer:")
            print("0 - Trabalhar")
            print("1 - Dormir")
            print("2 - Jogar")

            #recebe valor de entrada
            entrada = int(input("Digite uma das opções [0,1,2]:"))

            #como não se pode confiar em entradas dos usuários
            # (é assim que hackers geralmente tiram vantagem dos outros)
            # vamos checar a entrada antes de fazer algo com ela

            if type(entrada) == int and entrada in [0,1,2]:
                estadoAtual = estados[entrada]
                #agora que temos uma entrada válida, temos que sair do
                # laço atual, para permitir que o laço externo execute
                # para isso usamos o break
                break

            else:
                print("deu xabu, tente novamente")
                continue # executa de novo o menu para receber entrada

    # viu o que eu disse sobre funções serem usadas para deixar a lógica
    #   do programa mais arrumada?
    # só a impressão desse menu de entrada já atrapalha a observar o resto
    #   do comportamento do programa
    # fica como exercício tentar separar para uma outra função

    #como parar o laço infinito? quando a função tratamento_de_interrupção_pelo_teclado
    #  for executada, a variavel "paraEsseNegocio" será modificada para True, chamando
    #  um break e finalizando o programa
    if paraEsseNegocio == True:
        break

print("Nos vemos na próxima")