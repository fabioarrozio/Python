#exercicio 3 da lista para p1

count = 0
countv = 0


while True:
  p = input("Digite uma plavra: ")

  count += 1 #contador de palavras

  #verificar se começa com vogal
  ini = p[0]
  if ini == "a" or ini == "e" or ini == "i" or ini == "o" or ini == "u":
    countv += 1 #contador de vogal

  tam = len(p)
  print("A palavra {} tem {} letras".format(p, tam))

  for x in range (tam-1):
    print(p[x], '-', end='') # escreve as letras separadas por hifen

  vogais = 0
  for y in range (tam-1):  #contador de vogais na palavra digitada
    if p[y] == "a" or p[y] == "e" or p[y] == "i" or p[y] == "o" or p[y] == "u":
      vogais += 1

  #sem tratamento para letra maiscula e acentos.

  print(p[-1])  # pega a ultima letra
  print(p, "ao contrário é:", p[::-1])
  print("\n{} possui {} vogais".format(p, vogais+1))

  resp = str (input("\nDeseja digitar outrar palavra? (S/N): "))
  if resp.upper() != "S":
    break


print("\nTotal de palavras: {}".format(count))
print("Palavras iniciadas por vogal: {}".format(countv))

