def jeito_um():
    frases = input().split('. ')
    frasesNovas = ""


    for i in range(len(frases)):
        fraseNova = frases[i][0].capitalize() + frases[i][1:]

        if i != len(frases)-1:
            fraseNova += '. '
        frasesNovas += fraseNova


    print(frasesNovas)


def jeito_dois():
    frases = input()
    fraseNova = ""

    primeiraLetraAposPonto = True
    for letra in frases:
        if primeiraLetraAposPonto and letra != ' ':
            fraseNova += letra.capitalize()
            primeiraLetraAposPonto = False

        else:
            fraseNova += letra

        if letra in ".!?":
            primeiraLetraAposPonto = True


    print(fraseNova)

jeito_dois()