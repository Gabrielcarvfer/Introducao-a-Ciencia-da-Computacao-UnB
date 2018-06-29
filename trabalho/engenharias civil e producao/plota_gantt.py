from matplotlib import pyplot as plt
import random


def generate_colors(number_of_colors):
    return [[random.random(), #Red
             random.random(), #Green
             random.random(), #Blue
             random.random()  #Alpha/transparency
             ] for i in range(number_of_colors)]


def plota_gantt(tasks):
    #Cria uma figura para plotagem
    fig, ax = plt.subplots(figsize=(6, 3))

    #Cria uma série de cores para colorir as tarefas
    colors = generate_colors(len(tasks))

    #Cria uma lista para os nomes das tarefas (que serão impressas no gráfico)
    labels = []

    #De ordem decrescente do número da tarefa (para ficar ordenada na plotagem), plote
    for task in list(reversed(list(tasks.keys()))):
        #Guarda o número da tarefa
        labels.append(task)

        #Guarda os valores da tarefa (início e duração)
        data = [tasks[task]]

        #Cria uma barra na posição adequada
        ax.broken_barh(data, (len(tasks)-task - 0.4, 0.8), color=colors[task-1])

    #Número de barra, equivalente ao número de tarefas
    ax.set_yticks(range(len(labels)))

    #Associa labels da plotagem a lista com número das tarefas
    ax.set_yticklabels(labels)

    #Imprime legenda do eixo Y (vertical)
    ax.set_ylabel("Task number")

    #Imprime legenda do eixo X (horizontal)
    ax.set_xlabel("time [s]")

    #Configura layout
    plt.tight_layout()

    #Imprime gráfico
    plt.show()

#Se estiver executando esse arquivo, roda a função a seguir
#Senão, pula
if __name__ == "__main__":
    def main():
        # Dicionário endereçado (chaves) correspondentes ao número das tarefas
        #  com valores sendo momento de inicio e duração da respectiva tarefa
        tarefas = { 1 : [  0, 600],
                    2 : [  0, 300],
                    3 : [100, 100],
                    4 : [200, 200],
                    5 : [400, 400],
                    }
        plota_gantt(tarefas)
        pass

    main()
