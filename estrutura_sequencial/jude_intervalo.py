a, b = input().split()
c, d = input().split()
e = int(input())

a = int(a)
b = int(b)
c = int(c)
d = int(d)


if (e < a) and (e < b):

    print('Segundo intervalo!')

elif (e > c) and (e < d):

    print('Segundo intervalo!')

elif (e < a and e <= b) and e >= c and e < d:

    print('Ambos!')

else:

    print('Nenhum!')
