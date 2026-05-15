lista = [ " Arthur" ," Regis ", "Hiago "," Alexandre " ] 
print (lista)
index = int(input("escolha o index do aluno que voce dejesa(começa com 0 )"))
if index < 0 or index >(len(lista)- 1 ) :
    print ("o index que voce esvolheu nao esta presente na lista.")
else:
    print(lista[index ])    
