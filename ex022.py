while True:
    numero = int(input('Digite um número par ou impar: '))
    num = numero % 2

    if num == 0:
        print('Seu número é par!')
    else:
        print('Seu número é impar!')
    cont=input('Deseja tentar novamente? (s/n) ') .lower()
    if cont!="s":
        break