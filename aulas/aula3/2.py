nome = input("Digite nome:")
contador = 0
while nome != "fim" \
 and nome != "FIM" and nome != "Fim":
    contador = contador +1
    nome = input("Digite um nome:")

print("Total de nomes = ", contador)
