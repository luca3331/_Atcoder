N = int(input())
A = list(map(int, input().split()))
AA = sorted(A)
for n in range(len(AA) - 1):
    # print(AA[n], AA[n+1])
    if not AA[n] + 1 == AA[n + 1]:
        print(AA[n] + 1)
        break