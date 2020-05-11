count = 0
np = 0

while True:
    while True:
        try:
            num = int(input("Digite um número inteiro maior que 0: "))

            count += 1                                      #contador de números digitados

            if num % 2 == 1 and num >=3:
                print("{} é um número primo".format(num))
                np += 1                                     #contador de números primos

            else:
                print("{} não é número primo".format(num))
            break
        except:
            print("\nERRO: Digite apenas valor númerico")



    resp = input("\nDeseja digitar outro número ? (S/N): ")
    if resp.upper() != "S":
        print("Programa encerrado!")
        break
print("Quantidade de números digitados: {}".format(count))
print("\nQuantidade de números primos digitados: {}".format(np))
