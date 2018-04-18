#Lê entrada com input(), quebra numa lista com split()
# depois usa um laço para transformar numa lista de inteiros
lista = [int(x) for x in input().split()]

#Se a hora do fim é menor ou igual a do início, um dia se passou
#Exemplo: se o fim as 14h, e o inicio as 17h, só pode ser do outro dia
if lista[2] <= lista[0]:
    lista[2] += 24

#Se minutos do fim é menor que minutos do início, precisa-se tirar uma hora
# e adicionar minutos para fazer a diferença
#Exemplo: fim as 14:10, inicio as 13:50
if lista[3] < lista[1]:
    lista[3] += 60
    lista[2] -= 1

#Calcula diferença de horas
diffHoras   = lista[2] - lista[0]
diffMinutos = lista[3] - lista[1]

#Imprime resultado
print("O jogo durou", diffHoras, "hora(s) e", diffMinutos, "minuto(s)")