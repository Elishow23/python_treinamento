'''Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero). Para cada par lido, 
mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo o N e M).

Entrada
O arquivo de entrada contém um número não determinado de valores M e N. A última linha de entrada vai conter um número nulo ou negativo.

Saída
Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles, conforme exemplo abaixo.

Exemplo de Entrada	Exemplo de Saída
5 2
6 3
5 0

2 3 4 5 Sum=14
3 4 5 6 Sum=18'''

while True:

    n, m = input().split()
    n = int(n)
    m = int(m)

    if n <= 0 or m <= 0:
        break
    else:

        maior = 0
        menor = 0
        soma = 0

        if n > m:
            maior = n
            menor = m
        else:
            maior = m
            menor = n

        for i in range(menor, maior + 1):

            soma += i

            print(i, end=" ")
            
    print(f'Sum={soma}')
