import itertools, math

N = int(input())
S = list(map(int, input()))
P = [x for x in range(1, N + 1)]
memo = set()

ct = 0
for p in itertools.permutations(P, N):
    print(p)
    v = 0
    for i, pp in enumerate(p):
        v += S[pp - 1] * pow(10, N - i - 1)
    for nn in range(int(math.sqrt(v)) + 1):
        if nn ** 2 == v and not nn in memo:
            print(nn)
            memo.add(nn)
            ct += 1

print(ct)
