cont = int(input())

contador = 0

while True:

    if contador != cont:

        n = int(input())

        if n % 2 == 0:
            if n > 0:
                print('EVEN POSITIVE')
            elif n == 0:
                print('NULL')
            else:
                print('EVEN NEGATIVE')
        else:
            if n > 0:
                print('ODD POSITIVE')
            else:
                print('ODD NEGATIVE')

    else:
        break

    contador += 1
       
