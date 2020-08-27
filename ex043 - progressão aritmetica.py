primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiroTermo + 10 * razao
for contador in range (primeiroTermo, termo, razao):
    print(contador, end = ' ')
print('ACABOU')