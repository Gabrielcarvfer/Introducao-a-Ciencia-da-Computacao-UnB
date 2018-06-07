
fibs = {}
fibs[0] = 1
fibs[1] = 1

def fibonacci(x):
    if x in fibs.keys():
        return fibs[x]
    else:
        fibx = fibonacci(x-1) + fibonacci(x-2)
        fibs[x] = fibx
        return fibx


print(fibonacci(3))