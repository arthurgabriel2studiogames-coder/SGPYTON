import random
digite = 0
maximo=int(input("digite ate que numero voce deseja adivinhar: "))
chance=int(input("digite quantas chances "))
secreto = random.randint(1 , maximo)
while not(digite==secreto) and chance > 0:
    digite = int(input("digite um numero entre o 1 e o numero maximo: "))
    if digite==secreto :
        print("acertou")
    elif digite < secreto: 
        print("aumente")
        chance -= 1
    else:
        print("diminua")
        chance  -= 1
