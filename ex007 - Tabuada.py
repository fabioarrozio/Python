"""
este programa lê um número e mostra a tabuada deste numero
"""
while True:
    num=int(input("Informe o valor da tabuada: "))
    print("\n***Tabuada***")

    for i in range(1,11):
        print(num,'x',i,'=',num*i)
    resp=input("Deseja repetir? (s/n):")
    if resp!="s":
        break
