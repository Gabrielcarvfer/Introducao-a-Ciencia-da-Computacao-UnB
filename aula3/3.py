media=0
somador=0
contador=0
maxnota=0
minnota=11

nota=int(input("Digite uma nota: "))

while nota >= 0:
         somador = somador + nota
         contador = contador +1
         if maxnota<nota:
             maxnota = nota
         if minnota>nota:
             minnota = nota             
         nota=int(input("Digite a próxima nota: "))
         

if contador == 0:
    print("0")
else:
    media=somador/contador
    print(media)

print('A maior nota: ', maxnota)
print('A menor nota: ', minnota)
