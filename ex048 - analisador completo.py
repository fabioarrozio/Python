# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
# media de idade do grupo
# qual é o nome do homem mais velho
# quantas mulheres tem menos de 20 anos
nomevelho= ''
somaIdade = 0
maiorIdadehomem = 0
mediaIdade = 0
totmulher20 = 0
for contagem in range(1,5):
    nome=str(input('=== {}° pessoa === \nNome: '.format(contagem))).strip()
    idade=int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaIdade += idade
    if contagem == 1 and sexo in 'Mm':
        maiorIdadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maiorIdadehomem:
        maiorIdadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaIdade = somaIdade / 4
print('A media de idade do grupo é {} anos: '.format(mediaIdade))
print('O nome do homem mais velho é {} e tem {} anos'.format(nomevelho, maiorIdadehomem))
print('Existe(m) {} mulher(es) com menos de 20 anos'.format(totmulher20))