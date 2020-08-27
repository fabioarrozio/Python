nomeCompleto=input('digite seu nome: ') .strip()
nome = nomeCompleto.split()
print('Seu primeiro nome é {}' .format(nome[0]))
print('Seu ultimo nome é {}' . format(nome[len(nome)-1]))