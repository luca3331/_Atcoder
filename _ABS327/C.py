A = [input().split() for _ in range(9)]
check = [0 for _ in range(9)]

for r in range(9):
    for c in range(9):
        check[int(A[r][c]) - 1] += 1
    if check.count(1) != 9:
        print('No')
        exit()
    check = [0 for _ in range(9)]

for c in range(9):
    for r in range(9):
        check[int(A[r][c]) - 1] += 1
    if check.count(1) != 9:
        print('No')
        exit()
    check = [0 for _ in range(9)]

for i in range(3):
    for j in range(3):
        for ii in range(3):
            for jj in range(3):
                r = ii + i * 3
                c = jj + j * 3
                check[int(A[r][c]) - 1] += 1
        if check.count(1) != 9:
            print('No')
            exit()
        check = [0 for _ in range(9)]
print('Yes')