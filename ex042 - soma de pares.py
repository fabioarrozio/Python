soma = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        cont = cont + 1
        soma = soma + num
print('Você informou {} número(s) PAR(ES) e a soma foi {}'.format(cont,soma))
