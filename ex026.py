salario = float(input('Informe seu salário: R$'))
if salario >= 1250:
    aumento = (salario * 10) / 100
    print('Seu novo salário será: R${}'.format(salario + aumento))
else:
    aumento = (salario * 15) / 100
    print('Seu novo salário será: R${}'.format(salario + aumento))
