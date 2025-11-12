palavra = input()
#posicao = input()

palavra_mas = palavra.upper()

alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for l in palavra_mas:

    for al in alfabeto:

        if l == al:
            
            print(al)
            
            

    #for al in range(l, len(alfabeto), posicao):

        #print(al)