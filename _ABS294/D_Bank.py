from collections import deque

N, Q = map(int, input().split())
i = 1
call = deque()

for q in range(Q):
    if i > N and len(call) == 0:
        break
    E = input().split()
    if E[0] == '1':
        call.append(str(i))
        i += 1
    elif E[0] == '2':
        call.remove(E[1])
    else:
        print(call[0])
