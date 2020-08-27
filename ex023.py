viagem=float(input('quantos km terá sua viagem? '))
if viagem <= 200:
    valorViagem = (viagem * 0.50)
    print('Sua viagem irá custar R${:.2f}'.format(valorViagem))
else:
    valorViagem = (viagem * 0.45)
    print('Sua viagem irá custar R${:.2f}'.format(valorViagem))