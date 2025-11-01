import random

tentativa = 0

frase1 = 'Meus heróis Morreram de overdose Meus inimigos Estão no poder'

lista_frase = frase1.split()

random.shuffle(lista_frase)

valor = random.choice(lista_frase)

lista_frase.remove(valor)

print('Bem vindo ao Jogo das Palavras Secretas! Adivinhe que música é essa e informe a palavra que falta para completar a frase:')
print(lista_frase)

while True:

    tentativa += 1

    palavra = input()

    if tentativa == 3:
        print(f'Você atingiu número maxímo de tentativas. A frase é "{frase1}" e a palavra que faltava era "{valor}".')
        break

    elif palavra == valor:
        print(f'Parabés! a palavra que faltava era "{valor}". Confira a frase inteira:')
        print(frase1)
    else:
        print('Você errou, tente novamente!')




