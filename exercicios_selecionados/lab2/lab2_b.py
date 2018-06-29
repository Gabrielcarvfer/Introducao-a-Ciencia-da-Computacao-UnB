p = float(input())
h = float(input())

imc = p / (h*h)

peso_ideal = 24.9*(h*h)

#A lista abaixo tem elementos chamados de tuplas.
#Cada tupla tem diversos elementos, que podem ser homogêneos (mesmo tipo)
# ou heterogêneos (tipos diversos)
#Nas tuplas da lista, a primeira posição guarda o limite inferior do IMC,
# a segunda posição guarda o limite superior do IMC, a terceira posição
# guarda o que deve ser impresso, e a quarta posição guarda quando deve
# ser impresso o quando a pessoa deve perder de peso em quilos
limites = [( 0.0, 18.5, "Peso baixo"        , False),
           (18.5, 24.9, "Peso normal"       , False),
           (24.9, 29.9, "Sobrepeso"         , True ),
           (29.9, 34.9, "Obesidade grau I"  , True ),
           (34.9, 39.9, "Obesidade grau II" , True ),
           (39.9, 50.0, "Obesidade grau III", True )]

#No laço abaixo, cada tupla da lista limites é acessível por uma
# variável registro
for registro in limites:
    #Nesse if, o limite inferior e o superior de cada nível de IMC é testado
    if imc > registro[0] and imc <= registro[1]:
        #Caso dentre o limite correto, imprime o nível de IMC
        print(registro[2])
        #Nesse if, se checa caso haja sobrepeso e
        #  caso positivo, se imprime o peso a perder
        if registro[3]:
            print("%.2f" % (p - peso_ideal))
