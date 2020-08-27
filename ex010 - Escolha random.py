from random import choice
nome1=input('Digite o nome do primeiro aluno: ')
nome2=input('Digite o nome do segundo aluno: ')
nome3=input('Digite o nome do terceiro aluno: ')
nome4=input('Digite o nome do quarto aluno: ')

list = [nome1, nome2, nome3, nome4]
escolhido = choice(list)

print('o aluno escolhido foi {}!'.format(escolhido))