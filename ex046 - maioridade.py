for ano in range(0,7):
    data = int(input('Digite seu ano de nascimento: '))
    idade = 2020 - data
    if 2020 - data >= 18:
        print('Você nasceu no ano de {} e ja atingiu {} anos, é maior de idade!'.format(data, idade))
    else:
        print('Você nasceu no ano de {} e sua idade é {}, ainda é menor de idade!'.format(data, idade))