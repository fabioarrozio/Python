prova1 = float(input('Digite a nota de sua P1: '))
prova2 = float(input('Digite a nota de sua P2: '))
media = (prova1 + prova2) / 2
print(media)
if media < 5:
    print('REPROVADO!')
elif media >= 5 and media < 7:
    print('Recuperação!')
elif media >= 7:
    print('APROVADO!!!')