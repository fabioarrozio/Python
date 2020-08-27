numero = int(input('Digite um valor: '))
divisores = 0
for divisor in range(1, numero + 1):
    if numero % divisor == 0:
        divisores += 1
if divisores == 2:
    print('É primo!')
else:
    print('Não é primo!')
