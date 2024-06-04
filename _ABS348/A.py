N = int(input())
for n in range(1, N + 1):
    if n % 3 == 0:
        print('x', end='')
    else:
        print('o', end='')
