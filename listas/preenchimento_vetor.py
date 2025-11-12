v = [0]*10

n = int(input())

for i in range(len(v)):
    v[0] = n
    v[i] = v[i-1]*2

    #print(f'N[{i}] = {v[i]}')

for i in range(len(v)):
    print(f'N[{i}] = {v[i]}')
