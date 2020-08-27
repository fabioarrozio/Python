valorCasa = float(input('Qual o valor da casa? R$'))
valorSalario = float(input('Qual o seu salário? R$'))
pagamentoAnos = int(input('Em quantos anos você pretende pagar? '))

parcelaAno = valorCasa / pagamentoAnos
parcelaMes = parcelaAno / 12
parcelaTotal = pagamentoAnos * 12
valorParcelas = valorCasa / parcelaTotal

if valorParcelas > valorSalario * 0.3:
    print('Seu salário é de R${:.2f} e as parcelas custam R${:.2f} \nO valor da parcela ultrapassa 30% do seu salário!'.format(valorSalario,valorParcelas))
    print('Operação negada pelo banco!')
else:
    print('Número de parcelas são {}x'.format(parcelaTotal))
    print('O valor de suas parcelas será de R${:.2f}'.format(valorParcelas))
    print('Seu financiamento será aprovado!')