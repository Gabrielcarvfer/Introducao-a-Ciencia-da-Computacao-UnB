import csv

arquivo = csv.DictReader(open("teste.csv","r",encoding="utf8"))

print("Cabeçalhos/chaves dos dicionários")
print(arquivo.fieldnames)
print()

for linha in arquivo:
    print(linha)
    for campo in arquivo.fieldnames:
        print(campo, ':', linha[campo])
    print()