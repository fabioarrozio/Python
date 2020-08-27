ladoA=int(input('Digite o valor do lado A: '))
ladoB=int(input('Digite o valor do lado B: '))
ladoC=int(input('Digite o valor do lado C: '))
if ladoA < ladoB + ladoC and ladoB < ladoA + ladoC and ladoC < ladoA + ladoB:
    print('Seus valores formam um triangulo!')
else:
    print('Seus valores não formaram um triangulo!')