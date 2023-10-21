A, B, K = list(map(int, input().split()))
ct = 0
for i in reversed(range(1, min(A, B) + 1)):
    if A % i == 0 and B % i == 0:
        ct += 1
        if ct == K:
            print(i)

