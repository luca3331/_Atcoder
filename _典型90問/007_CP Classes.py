from bisect import bisect_left
N = int(input())
A = sorted(list(map(int, input().split())))
Q = int(input())
for q in range(Q):
    B = int(input())
    index = bisect_left(A, B)
    if index == 0:
        print(A[0] - B)
    elif index == N:
        print(B - A[-1])
    else:
        print(min(B - A[index - 1], A[index] - B))
