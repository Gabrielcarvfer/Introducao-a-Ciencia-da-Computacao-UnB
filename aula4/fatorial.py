def fatorial_iterativo(n):
    fatorial = 1
    for i in range(1,n+1):
        fatorial *= i
    return fatorial


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

def teste():
    n_fatoriais = [1,2,3,4,5,6,7,8,9,10]
    resultado_fatoriais = [1,2,6,24,120,720,5040,40320,362880,3628800]
    acertou_fatoriais = []

    acertos = 0
    erros   = 0
    for i in range(len(n_fatoriais)):
        res = fatorial_recursivo(n_fatoriais[i])
        if res != resultado_fatoriais[i]:
            acertou_fatoriais.append(False)
            erros += 1
        else:
            acertou_fatoriais.append(True)
            acertos += 1

    print("O teste passou em", acertos,"e falhou em", erros, "de", len(n_fatoriais),"valores testados")

def teste2():
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
    for tupla in n_fatoriais:
        res = fatorial_recursivo(tupla[0])
        if res != tupla[1]:
            erros += 1
        else:
            tupla[2] = True
            acertos += 1

    print("O teste passou em", acertos,"e falhou em", erros, "de", len(n_fatoriais),"valores testados")

teste2()