# vetor/lista contendo valores dos diferentes tipos de cédulas
cedulas = [100,50,20,10,5,2,1]

# é possível acessar os valores de cada tipo de cédula a partir de um índice
# o índice é a posição no qual o valor se encontra
# cedulas[0] = 100
# cedulas[1] = 50
# cedulas[2] = 20
# e assim por diante

# vetor/lista contendo número de cédulas de cada valor
# inicializado como [0,0,0,0,0,0,0], com um 0 para cada tipo de nota
# comando len() retorna o tamanho do vetor(lista) passado(a)
notas = [0]*len(cedulas)

valorEntrada = int(input("Digite um valor: "))

for posicao in range(len(cedulas)):
    # posicao varia de 0 a tamanho da lista 'cedulas' - 1

    # notas[posicao] guarda o número de notas de cada tipo de cedula
    notas[posicao] = valorEntrada//cedulas[posicao]

    # remove de valorEntrada os valores multiplos de cedulas[posicao]
    # quando posicao = 0, cedulas[0] = 100, portanto múltiplos de 100 são removidos
    valorEntrada = valorEntrada % cedulas[posicao]

    # imprime número de notas, seguido de " notas de R$ ", o valor do tipo de nota em cedulas[posicao]...
    print(notas[posicao]," notas de R$ ",cedulas[posicao],",00",sep="")