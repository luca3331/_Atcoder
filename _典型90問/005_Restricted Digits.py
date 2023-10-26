from itertools import product
N, B, K = list(map(int, input().split()))
C = input().split()
# print(C)
ct = 0
for item in product(C, repeat=N):
    num = int(''.join(item))
    if num % B == 0:
        ct += 1
        ct = ct % (10**9 + 7)
print(ct)