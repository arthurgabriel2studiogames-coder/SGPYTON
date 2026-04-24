digite = 0
secreto = 7
while not(digite==secreto):
    digite = int(input("digite um numero entre 1 a 10: "))
    if digite==secreto :
        print("acertou")
    elif digite < secreto: 
        print("aumente")
    else:
        print("diminua")
