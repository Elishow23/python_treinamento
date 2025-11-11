x = int(input())
y = int(input())

somador = 0

for i in range(y+1, x):
    if i % 2 != 0:
        somador += i

print(somador)