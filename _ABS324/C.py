from collections import deque
N, TT = input().split()
for i in range(int(N)):
    S = deque(input())
    T = deque(TT)
    change = 0
    flag = True
    while len(S) and len(T):
        if change > 2:
            flag = False
            break
        if not S[0] == T[0]:
            T.popleft()
            change += 1
        else:
            T.popleft()
            S.popleft()
    if flag:
        print(i + 1)



