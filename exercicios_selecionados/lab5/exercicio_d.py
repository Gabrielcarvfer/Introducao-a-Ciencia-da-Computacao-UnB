num_linhas = int(input())

P = 0
U = 0

for i in range(num_linhas):

    frase = input()

    for letra in frase:
        if letra == 'u' or letra == 'U':
            U += 1
        if letra == 'p' or letra == 'P':
            P += 1

print("%d %d" % (P,U))