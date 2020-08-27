print('\033[1;32m-=\033[m'*14)
print('Números pares entre 1 e 50:')
print('\033[1;32m-=\033[m'*14)
resp = input('Iniciar? [S/N] :').lower()
if resp == 's':
    for x in range(2, 51, +2):
        print(x)
    print('\033[1;32m-=\033[m' * 2)
    print('Fim')
    print('\033[1;32m-=\033[m' * 2)
else:
    print('\033[1;32m-=\033[m' * 2)
    print('Fim')
    print('\03n3[1;32m-=\033[m' * 2)