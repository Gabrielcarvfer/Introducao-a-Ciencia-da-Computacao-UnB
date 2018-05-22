#No fatorial iterativo, multiplicamos todos os números de 1 até n em um laço
def fatorial_iterativo(n):
    fatorial = 1
    for i in range(1,n+1):
        fatorial *= i
    return fatorial

#No fatorial_recursivo(n), chamamos a função que multiplica n e o resultado de fatorial_recursivo(n-1)
#No fatorial_recursivo(n-1), chamamos a função que multiplica n-1 e o resultado de fatorial_recursivo(n-2)
#E assim até a condição de parada ser alcançada, com n <= 1
def fatorial_recursivo(n):
    if n <= 1:
        return 1
    else:
        return n*fatorial_recursivo(n-1)

def main():
    n = 10
    fatIte = fatorial_iterativo(n)
    fatRec = fatorial_recursivo(n)
    print("Fatorial de n =", n, ": recursivo =", fatRec,"; iterativo =", fatIte)


#Exemplificando dois tipos de testes abaixo
def teste():
	#Neste teste, temos uma lista com o número de n's, para os quais calcularemos n!
    n_fatoriais = [1,2,3,4,5,6,7,8,9,10]

    #Na seguinte lista, o resultado obtido externamente para os fatoriais para os mesmos n acima,
    # em mesma ordem
    resultado_fatoriais = [1,2,6,24,120,720,5040,40320,362880,3628800]

    #Na lista seguinte, uma lista vazia que guarda os resultados (verdadeiro ou falso) se 
    # a resposta calculada bate com os resultados para cada n verificado, também
    # em mesma ordem
    acertou_fatoriais = []

    #Duas variaveis contadoras para sabermos quantos passaram e quantos falharam
    acertos = 0
    erros   = 0

    #No laço a seguir, executamos o cálculo e checagem para os k-ésimos casos de teste
    # onde k = tamanho da lista n_fatoriais ( ou seja len(n_fatoriais) em python)
    #Cada i indica a posição tanto do n a ser calculado em n_fatoriais, quanto
    # do resultado esperado em resultado_fatoriais 
    for i in range(len(n_fatoriais)):

    	#Para cada valor assumido por i (0 até 9)
    	# res = fatorial(n_fatoriais[i]) onde, para i = 0,
    	# fatorial(n_fatoriais[0]) = fatorial(1), onde 1 é o primeiro elemento 
    	# (no python contagens começam no 0) da lista n_fatoriais
        res = fatorial_recursivo(n_fatoriais[i])

        #Verifica se o resultado calculado bate com o esperado
        if res != resultado_fatoriais[i]:

        	#Caso não bata, marque como reprovado (falso) e conte o erro
            acertou_fatoriais.append(False)
            erros += 1

        else:

        	#Caso bata, marque como aprovado (verdadeiro) e conte o acerto
            acertou_fatoriais.append(True)
            acertos += 1

    print("O teste passou em", acertos,"e falhou em", erros, "de", len(n_fatoriais),"valores testados")

def teste2():
	#Nesse tipo de organização, o número n, o resultado esperado de n! 
	# e se o resultado passou no teste ou não estão unidos numa
	# estrutura chamada tupla (elementos heterogêneos a.k.a. tipos diferentes)
	#A lista n_fatoriais é composta por uma lista [] de tuplas ()

    n_fatoriais = [(1,1       ,False),
                   (2,2       ,False),
                   (3,6       ,False),
                   (4,24      ,False),
                   (5,120     ,False),
                   (6,720     ,False),
                   (7,5040    ,False),
                   (8,40320   ,False),
                   (9,362880  ,False),
                   (10,3628800,False)]
    acertos = 0
    erros   = 0

    #Ao invés de o laço ser em função da posição dentro de 0 e tamanho do vetor-1
    # aqui o laço trabalha em termo de tuplas, que são copiadas para a variavel tupla
    #A partir dela, com o indice interno dos elementos, se acessam todos os valores
    # contidos dentro da tupla
    #Na posição 0 se tem o valor de n, na posição 1 se tem o valor de n! esperado
    # e na posição 2 se tem o estado de aprovação no teste
    for tupla in n_fatoriais:
    	#Aqui dentro tupla pode assumir qualquer um dos valores entre parenteses 
    	# da lista n_fatoriais

    	#Res recebe fatorial(tupla[0]) = fatorial(1) para a primeira tupla da lista
        res = fatorial_recursivo(tupla[0])

        #Se a resposta res seja diferente do valor em tupla[1] = 1, então conta um erro
        if res != tupla[1]:
            erros += 1
        else:
        	#Caso seja igual, muda o estado de aprovação do teste para verdadeiro e
        	# conta o acerto
            tupla[2] = True
            acertos += 1

    print("O teste passou em", acertos,"e falhou em", erros, "de", len(n_fatoriais),"valores testados")

teste2()