while True:
    print('Olá humano, acabo de pensar em um número de 0 a 10 e quero saber se consegue adivinhar!')
    num=int(input('Digite o número que você acha que pensei: '))
    if num == 5:
        print('ACERTOU!!!')
    else:
        print('ERROU!!!')
    resp=input('Deseja tentar novamente? (S/N)') .lower()
    if resp!='s':
        break
