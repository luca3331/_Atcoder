from collections import Counter
N, Q = input().split()
T = list(map(int, input().split()))
single = Counter(T)
print(int(N) - len([x for x in single.keys() if single[x] % 2 == 1]))
