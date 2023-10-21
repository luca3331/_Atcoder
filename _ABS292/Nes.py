N = int(input())

A = [a for a in range(1, N + 1)]

for n in range(2, N + 1):
    for i in range(len(A)):
        if A[i] % n == 0:
            A[i] = -1

for i in range(1, N):
    if A[i] != -1:
        print(A[i])

