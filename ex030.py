num1=int(input('Digite o primeiro valor: '))
num2=int(input('Digite o segundo valor: '))
if num1 > num2:
    print('O primeiro valor "{}" é maior que o segundo valor "{}"'.format(num1,num2))
elif num1 < num2:
    print('O segundo valor "{}" é maior que o primeiro valor "{}"'.format(num2,num1))
else:
    print('0 primeiro valor e o segundo valor são iguais')