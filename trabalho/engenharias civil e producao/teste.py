import csv

arquivo = csv.DictReader(open("Tarefas.csv","r",encoding="utf8"))

print("Cabeçalhos/chaves dos dicionários")
print(arquivo.fieldnames)
print()
dicionario_tarefas = {}

#Primeiro lemos todos as tarefas num dicionário
for linha in arquivo:
    tarefa = {}
    for campo in arquivo.fieldnames:
        tarefa[campo] = linha[campo]

    if len(tarefa[campo]) > 0:
        tarefa[campo] = [int(strings) for strings in tarefa[campo].split()]
    tarefa[arquivo.fieldnames[1]] = int(tarefa[arquivo.fieldnames[1]])
    tarefa[arquivo.fieldnames[0]] = int(tarefa[arquivo.fieldnames[0]])


    dicionario_tarefas[int(linha["Índice tarefa"])] = tarefa
    pass

#Depois buscamos a maior sequencia de saltos em duração e guardamos a sequencia de saltos, recursivamente
maior_sequencia = [0,[1]] #sequencia inicial tem duração 0 e começa do 1

def custo_recursivo(duracao_atual, caminho_atual):
    if duracao_atual > m

for tarefa in dicionario_tarefas:
    custo_recursivo(tarefa, [tarefa])