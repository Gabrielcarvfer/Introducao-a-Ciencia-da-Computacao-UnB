frase = input()
fraseTraduzida = ""

consoantesMin = 'bcdfghjklmnpqrtsvwxyz'
consoantesMax = 'BCDFGHJKLMNPQRSTVWXYZ'

for i in range(len(frase)):
    if frase[i] in consoantesMin:
        fraseTraduzida += 'p'
    elif frase[i] in consoantesMax:
        fraseTraduzida += 'P'
    else:
        fraseTraduzida += frase[i]

print(fraseTraduzida)