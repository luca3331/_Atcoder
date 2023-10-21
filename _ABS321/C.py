K = int(input())
ct = 9
flag = False
T = [[0 for x in range(9)] for _ in range(9)]
if K < 10:
    print(K)
else:
    for i in range(9):
        T[0][i] = 1
    for r in range(1, 9):
        for c in range(9):
            if c + 1 >= r:
                T[r][c] = sum(T[r - 1][:c + 1])
                if ct + T[r][c] >= K:
                    flag = True
                    break
                ct += T[r][c]
        if flag:
            break

    print(T)

