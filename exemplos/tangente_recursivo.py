#Para entender de onde saiu a função tangente
# fica o vídeo do Mathologer https://www.youtube.com/watch?v=Lk_QF_hcM8A
#
# tan(x) =                   x
#          -----------------------------------------
#           1 - x^2
#              -------------------------------------
#               3 - x^2
#                  ---------------------------------
#                   5 - x^2
#                      -----------------------------
#                       7 - x^2
#                          -------------------------
#                           9 - x^2
#                              ---------------------
#                               11 - x^2
#                                   ----------------
#                                     13 - x^2
#                                         ----------
#                                           15 - x^2
#                                               ----
#                                                ...


PI = 3.14159265359


#Define função recursiva da tangente
def tan_recursion(den, level, maxLevel, radQuadrado):
    if level < maxLevel:
        valor_calculado = den - radQuadrado / tan_recursion(den+2,level+1,maxLevel,radQuadrado)
    else:
        valor_calculado = den
    return valor_calculado


#Define função tangente
def tan(rad, maxLevel):
    radQuadrado = rad*rad #calcula o quadrado
    if rad == 0.0:
        return 0.0
    valor_calculado = rad / tan_recursion(1, 0, maxLevel,radQuadrado)
    return valor_calculado

#Define função que converte graus em radianos
def grau_para_rad(angulo):
    return angulo*PI/180


#Define função principal
def main():
    #Calcula dois exemplos de tangente recursivo com 100 iterações
    print("Tangente de Pi/4 é %.2f" % tan(grau_para_rad(45),10))
    print("Tangente de Pi/2 é %.2f" % tan(grau_para_rad(90),10))

    #Cria lista com valores de -180 a 175, a cada 5 (-180,-175,-170,...)
    intervalo_impressao = list(range(-180, 180, 5))

    #Cria lista para guardar valores de tangente calculados
    valores_tangente = []
    valores_tangente_recursivo = [[],[],[],[],[]]

    #Importa biblioteca matemática para calcular a tangente
    import math

    #Para cada um dos ângulos na lista intervalo_impressão
    for angulo in intervalo_impressao:
        # Transformamos o ângulo em radianos
        rads = grau_para_rad(angulo)

        #Calculamos a tangente do ângulo com a biblioteca matemática
        valores_tangente.append(math.tan(rads))

        #Calculamos a tangente recursiva dos mesmos ângulos
        # com 1,3,5,7,9 chamadas recursivas e guardamos nas listas apropriadas
        for i in range(5):
            valores_tangente_recursivo[i].append(tan(rads, (i+1)*2-1))

    #Importamos a biblioteca gráfica
    import matplotlib.pyplot as pyplot

    #Plotamos os valores calculados pela biblioteca matemática
    pyplot.plot(intervalo_impressao, valores_tangente, 'green')


    cores = ["purple","blue","orange","turquoise","red"]
    #Plotamos os valores calculados pela função de tangente recursiva, cada uma com uma cor
    for i in range(5):
        pyplot.plot(intervalo_impressao, valores_tangente_recursivo[i], cores[i])

    #Limitamos a área de plotagem de -Pi a Pi (eixo X), e -10 a 10 (eixo Y)
    pyplot.axis([-180, 180, -10, 10])

    #Imprimimos os valores plotados em tela, abrindo a janela com os valores plotados
    pyplot.show()
    return


#Chama função
#main()