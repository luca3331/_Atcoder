N, X = map(int, input().split())
A = set(map(int, input().split()))
flag = False
for Ai in A:
    if Ai - X in A:
        flag = True
        break
if flag:
    print('Yes')
else:
    print('No')


