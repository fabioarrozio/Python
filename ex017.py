# Fatiamento de String, Análise com len(), count(), find(),
# transformações com replace(), upper(), lower(),
# capitalize(), title(), strip(), junção com join().


palavra=input('Digite uma palavra ou frase: ') .upper() .strip()
letra=input('Digite uma letra que você queira encontrar: ') .lower() .upper()
print('A letra {} aparece {} vezes.'.format(letra, palavra.count(letra)))
print('A primeira vez que aparece sua letra é na posição {}' .format(palavra.find(letra)+1))
print('A ultima vez que aparece sua letra é na posição {}' .format(palavra.rfind(letra)+1))