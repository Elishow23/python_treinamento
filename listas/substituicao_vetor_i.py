x = [1]*10

for i in range(len(x)): # O len da o tamanho do vetor, o range visita o tamanho, um por um.

    n = int(input())

    if n > 0:
        x[i] = n

    print(f'X[{i}] = {x[i]}')
        
    
