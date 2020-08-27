while True:
    ano=int(input('Digite o ano: '))
    num = ano % 4
    if num == 0:
        print('Ano bissexto')
    else:
        print('ano normal')
        resp=input('Deseja tentar novamente? (s/n): ')
    if resp!='s':
        break