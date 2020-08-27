ladoA = float(input('Primeiro valor: '))
ladoB = float(input('Segundo valor: '))
ladoC = float(input('Terceiro valor: '))
if ladoA < ladoB + ladoC and ladoB < ladoA + ladoC and ladoC < ladoA + ladoB:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if ladoA == ladoB == ladoC:
        print('EQUILÁTERO!')
    elif ladoA != ladoB != ladoC != ladoA:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os valores acima NÃO FORMAM TRIANGULO ALGUM!')