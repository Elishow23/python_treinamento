'''Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no sistema cartesiano. Para cada ponto escrever o quadrante a que ele pertence. 
O algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA (nesta situação sem escrever mensagem alguma).

Entrada
A entrada contém vários casos de teste. Cada caso de teste contém 2 valores inteiros.

Saída
Para cada caso de teste mostre em qual quadrante do sistema cartesiano se encontra a coordenada lida, conforme o exemplo.

Exemplo de Entrada	Exemplo de Saída
2 2
3 -2
-8 -1
-7 1
0 2

primeiro
quarto
terceiro
segundo'''

quadrante = []

while True:

    x, y = input().split()

    x = int(x)
    y = int(y)

    if x == 0 or y == 0:
        break
    else:

        if x > 0 and y > 0:
            quadrante.append('primeiro')
        elif x > 0 and y < 0:
            quadrante.append('quarto')
        elif x < 0 and y > 0:
            quadrante.append('segundo')
        elif x < 0 and y < 0:
            quadrante.append('terceiro')

for i in quadrante:
    print(i)