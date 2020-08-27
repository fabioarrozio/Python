print('\033[7mA Confederação Nacional de Natação quer saber sua idade para te encaixar em uma categoria de competidores!\033[m')
anoNascimento = int(input('Digite o ano de nascimento: ',))
idade = 2020 - anoNascimento
if idade <= 9:
    print('Tem {} anos'.format(idade))
    print('Você fará parte da catêgoria \033[7mMIRIM\033[m')
elif idade <= 14:
    print('Tem {} anos'.format(idade))
    print('Você fará parte da catêgoria \033[7mINFANTIL\033[m')
elif idade <= 19:
    print('Tem {} anos'.format(idade))
    print('Você fará parte da catêgoria \033[7mJUNIOR\033[m')
elif idade == 20:
    print('Tem {} anos'.format(idade))
    print('Você fará parte da catêgoria \033[7mSÊNIOR\033[m')
else:
    print('Tem {} anos'.format(idade))
    print('Você fará parte da catêgoria \033[7mMASTER\033[m')