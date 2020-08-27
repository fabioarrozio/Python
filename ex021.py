velocidade=float(input('Qual a velocidade que você passou pelo radar? '))
if velocidade >= 80:
    print('Você ultrapassou o limite de velocidade!')
    multa = (velocidade * 7)
    print('Multa estipulada: R${:.2f}'.format(multa))
else:
    print('Velocidade normal, pode prosseguir!')