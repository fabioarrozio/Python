ini = int(input("Digite o valor inicial: "))
fim = int(input("Digite o valor final: "))
passo = int(input("Digite o passo: "))

for x in range (ini,fim,passo):
    print(x, " ", end="")
