altura = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('seu IMC é {:.1f}, você está abaixo do peso'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('seu IMC é {:.1f}, você está no seu peso ideal'.format(imc))
elif imc >= 25 and imc < 30:
    print('seu IMC é {:.1f}, você está em sobrepeso'.format(imc))
elif imc >= 30 and imc < 40:
    print('seu IMC é {:.1f}, você está com obesidade'.format(imc))
else:
    print('seu IMC é {:.1f}, você está com obesidade mórbida'.format(imc))