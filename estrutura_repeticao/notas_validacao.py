opcao = 0

while True:
    if opcao == 2:
        break
    else:

        nota1 = int(input())
        if nota1 < 0 or nota1 > 10:
            print('nota invalida')
        nota2 = int(input())
        if nota2 < 0 or nota2 > 10:
            print('nota invalida')

        media = nota1 + nota2 / 2

        print(f'media = {media:.2f}')

        opcao = int(input("novo calculo (1-sim 2-nao)"))