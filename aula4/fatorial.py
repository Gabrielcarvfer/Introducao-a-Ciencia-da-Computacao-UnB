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

n = 10
fatIte = fatorial_iterativo(n)
fatRec = fatorial_recursivo(n)
print("Fatorial de n =", n, ": recursivo =", fatRec,"; iterativo =", fatIte)