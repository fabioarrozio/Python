while True:
    num1=int(input("Digite um valor: "))
    num2=int(input("Digite outro valor:"))
    if (num1 > num2):
        print(num1,"é maior que ",num2)
    if (num2 > num1):
        print(num2,"é maior que ",num1)
    resp=input("Deseja repetir? (s/n):")
    if resp!="s":
        break
