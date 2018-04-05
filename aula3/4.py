n = int(input("Digite numero"))
x = 1
fat = 1
while x <= n:
    fat = fat*x
    x = x + 1
    print("fat=",fat)
    print("x=",x)

print("O fatorial de ",n," é ", fat)
