anoDeNascimento = int(input('Digite o ano em que nasceu: '))
sexo = input('Informe seu gênero: [M/F] ').lower()
if sexo == 'f':
    print('Mulheres não precisam se alistar obrigatóriamente!')
else:
    idade = (2020 - anoDeNascimento)
    if idade < 18:
        falta = 18 - idade
        print('Faltam {} anos! Sua hora de se alistar para o Exercito Brasileiro vai chegar!'.format(falta))
    elif idade == 18:
        print('Ja chegou sua hora de se alistar para o Exercito Brasileiro!')
    else:
        passou = idade - 18
        print('passaram {} ano(s) de se alistar para o Exercito Brasileiro!'.format(passou))
