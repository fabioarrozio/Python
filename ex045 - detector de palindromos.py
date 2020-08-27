palindromo = str(input('Digite sua frase: ')).strip() .upper()
palavras = palindromo.split()
junto = ''.join(palavras)
invertido = ''
for letra in range(len(junto) - 1, -1, -1):
    invertido += junto[letra]
print(junto)
if invertido == junto:
    print('é um palindromo')
else:
    print('não é um palindromo')