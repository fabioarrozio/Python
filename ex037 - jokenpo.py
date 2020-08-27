from random import choice
from time import sleep
while True:
    print('''      =======================
      ========JOKENPÔ========
      =======================''')
    jogada = int(input('''Selecione a sua jogada!
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
: '''))
    sleep(1)
    print('\033[7mJO\033[m', end='')
    sleep(1)
    print('\033[7mKEN\033[m', end='')
    sleep(1)
    print('\033[7mPÔ\033[m')


    Pedra = 1
    Papel = 2
    Tesoura = 3

    list = [1 , 2 , 3]
    escolhido = choice(list)
    if jogada == 1:
        print('Sua jogada foi \033[7m PEDRA \033[m')
        if escolhido == 1:
            print('CPU jogou \033[1;30;41m PEDRA \033[m, EMPATE!')

        elif escolhido == 2:
            print('\033[1;30;41m PAPEL \033[m cobre \033[7m PEDRA \033[m, você perdeu!')

        elif escolhido == 3:
            print('\033[7m PEDRA \033[m quebra \033[1;30;41m TESOURA \033[m, você ganhou!!!')

    elif jogada == 2:
        print('Sua jogada foi \033[7m PAPEL \033[m')
        if escolhido == 1:
            print('\033[7m PAPEL \033[m cobre \033[1;30;41m PEDRA \033[m você ganhou!!!')

        elif escolhido == 2:
            print('CPU jogou \033[1;30;41m PAPEL \033[m, EMPATE!')

        elif escolhido == 3:
            print('\033[1;30;41m TESOURA \033[m corta \033[7m PAPEL \033[m, você perdeu!')

    elif jogada == 3:
        print('Sua jogada foi \033[7m TESOURA \033[m')
        if escolhido == 1:
            print('\033[1;30;41m PEDRA \033[m quebra \033[7m TESOURA \033[m você perdeu!')

        elif escolhido == 2:
            print('\033[7m TESOURA \033[m corta \033[1;30;41m PAPEL \033[m, você ganhou!!!')

        elif escolhido == 3:
            print('CPU jogou \033[1;30;41m TESOURA \033[m, EMPATE!')
    resp = input('Jogar novamente? [S/N]').lower()
    if resp != 's':
        break