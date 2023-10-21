N = int(input())
yakusu = [x for x in range(1, 10) if N % x == 0]

for i in range(N + 1):
    flag = False
    for j in yakusu:
        if i % (N / j) == 0:
            flag = True
            print(j, end="")
        if flag:
            break
    if not flag:
        print('-', end="")