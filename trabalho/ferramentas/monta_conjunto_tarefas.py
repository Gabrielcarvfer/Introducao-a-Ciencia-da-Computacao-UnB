import random
tarefas = []



for num_tarefa in range(1,200):
    lista_requisitos = {}

    if num_tarefa > 1:
        for num_requisitos in range(random.randint(1,num_tarefa-1)):
            req = random.randint(1,num_tarefa-1)
            if req not in lista_requisitos.keys():
                lista_requisitos[req] = 0

    nova_tarefa = [num_tarefa,random.randint(100, 7200),list(lista_requisitos.keys())]
    tarefas.append(nova_tarefa)
    print(nova_tarefa)

#print(tarefas)