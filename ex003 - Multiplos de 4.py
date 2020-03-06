f=int(input("Valor final: "))
cont=1
while cont<=f:
    if cont%4==0:
        print(' ',"pim", end='')
    else:
        print(' ', cont, end='')
    cont+=1
