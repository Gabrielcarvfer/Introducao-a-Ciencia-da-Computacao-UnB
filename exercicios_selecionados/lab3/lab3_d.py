#Lê a quantidade de casos de teste
n = int(input())

maior_soma = -999999999999999999999999
menor_soma =  999999999999999999999999

#Executa os casos de teste
for _ in range(n):
    #Lê X e Y
    x,y = input().split()
    x,y = int(x),int(y)

    #Checa se X é par, soma 1, tornando ímpar
    if x % 2 == 0:
        x += 1

    soma = 0

    #Adiciona X a soma, depois incrementa X em 2 (próximo ímpar)
    for _ in range(y):
        soma += x
        x += 2

    #Verifica se soma é maior que maior_soma
    if soma > maior_soma:
        maior_soma = soma

    #Verifica se soma é menor que menor_soma
    if soma < menor_soma:
        menor_soma = soma

    #Imprime soma
    print(soma)

#Imprime maior e menor soma. mais a média
print(maior_soma)
print(menor_soma)
print("%0.2f" % ((maior_soma + menor_soma)/2))