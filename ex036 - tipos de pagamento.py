valorProduto = float(input('Digite o valor do produto a ser pago: R$'))
formaPagamento = int(input('''Escolha a forma de pagamento: 
\033[7m[ 1 ]\033[m Dinheiro (10% de desconto)
\033[7m[ 2 ]\033[m Cartão                    '''))

if formaPagamento == 1:
    descProduto = valorProduto - (valorProduto * 10/100)
    print('Seu produto sairá por R${} com 10% de desconto no pagamento a vísta em dinheiro!'.format(descProduto))

elif formaPagamento == 2:
    formaCartao = int(input('''Escolha a forma de pagamento por cartão: 
\033[7m[ 1 ]\033[m A vísta (5% de desconto)
\033[7m[ 2 ]\033[m em 2x sem juros         
\033[7m[ 3 ]\033[m em 3x ou mais com juros de 20%    '''))

    if formaCartao == 1:
        descCartao = valorProduto - (valorProduto * 5/100)
        print('\033[7mSeu produto saíra por R${:.2f} com 5% de desconto no pagamento a vista com cartão!\033[m'.format(descCartao))

    elif formaCartao == 2:
        parcelamento = valorProduto / 2
        print('\033[7mSeu produto saíra em 2 parcelas de R${:.2f} sem juros no cartão!\033[m'.format(parcelamento))

    elif formaCartao == 3:
        numParcelas = int(input('Quantas parcelas deseja fazer? '))
        acresCartao = valorProduto + (valorProduto * 20 / 100)
        parcelamento = acresCartao / numParcelas
        print('\033[7mSeu produto saíra em {} parcelas de R${:.2f} com juros de 20% no cartão! Totalizando R${} no valor final.\033[m'.format(numParcelas,parcelamento,acresCartao))

    else:
        print('\033[1;30;41mForma invalida, reinicie a operação!\033[m')

else:
    print('\033[1;30;41mForma invalida, reinicie a operação!\033[m')