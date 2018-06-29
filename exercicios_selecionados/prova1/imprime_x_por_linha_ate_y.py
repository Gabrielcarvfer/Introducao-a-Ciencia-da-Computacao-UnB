

def tipo_1(num_atual, resto, X, Y):
    while num_atual < (Y-resto):
        numeros = ""
        for i in range(X):
            numeros = numeros + str(num_atual) + " "
            num_atual += 1
        print(numeros)

    if resto != 0:
        numeros = ""
        for i in range(resto):
            numeros = numeros + str(num_atual) + " "
            num_atual += 1
        print(numeros)


def tipo_2(num_atual, X, Y):
    continua = True
    while continua:
        numeros = ""

        #Para impressão após a iteração seguinte
        if Y < 0:
            continua = False

        #Imprime ou X ou Y % X
        for i in range(min(X,Y)):
            numeros = numeros + str(num_atual) + " "
            num_atual += 1
        print(numeros)

        Y -= X


def main():
    X = 3
    Y = 100
    # X = int(input())
    # Y = int(input())

    num_atual = 1
    resto = Y % X

    #tipo_1(num_atual,resto, X, Y)
    tipo_2(num_atual,X,Y)

main()