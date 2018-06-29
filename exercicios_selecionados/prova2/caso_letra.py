string_entrada = "camelCase_mixed"


string_saida =""
posicao_letra = 0
letra_anterior = ""

for letra in string_entrada:
    if posicao_letra == 0:
        string_saida += letra.capitalize()
        posicao_letra += 1
        letra_anterior = letra
        continue

    if letra in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and letra_anterior not in "_":
        string_saida += "_"+letra
        letra_anterior = letra
        continue

    if letra in "abcdefghijklmnopqrstuvwxyz" and letra_anterior in "_":
        string_saida += letra.capitalize()
        letra_anterior = letra
        continue

    string_saida += letra
    letra_anterior = letra

print(string_saida)

