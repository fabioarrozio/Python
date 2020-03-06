while True:
    gen = input("Qual é o seu gênero? \n[F] Feminino \n[M] Masculino \n[O] Outro \n: ")
    if (gen == 'F' or gen == 'f'):
        print("Sexo feminino.")
        break
    if (gen == 'M' or gen == 'm'):
        print("Sexo masculino.")
        break
    if (gen == 'O' or gen == 'o'):
        print("Outro.")
        break
    print("Informação invalida, tente novamente \n")
