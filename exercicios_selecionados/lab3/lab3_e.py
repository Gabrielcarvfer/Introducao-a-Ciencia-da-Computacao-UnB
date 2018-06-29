#Somente a demonstração de como se calcular fibonacci

#Calcula fibonacci de n
def fibonacci(n):
    #Uma lista com valores iniciais de fibonacci
    fibonacci_lista = [1,1]
    
    #Soma fibonnaci(n-1) + fibonacci(n) e guarda em fibonacci(n+1)
    for posicao in range(1,n):
        fibonacci_lista.append(fibonacci_lista[posicao]+fibonacci_lista[posicao-1])
        
    #Retorna fibonacci de n
    return fibonacci_lista[n]

