from collections import deque
S = deque()
Q = int(input())
for i in range(Q):
    q = input().split()
    if q[0] == '1':
        S.append(q[1])
    if q[0] == '2':
        S.popleft()
    if q[0] == '3':
        print(int(list(S)) % 998244353)