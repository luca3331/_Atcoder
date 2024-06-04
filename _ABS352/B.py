from collections import deque
S = deque(list(input()))
T = deque(list(input()))
collect_pos = []
t_pos = 0
for s in S:
    while True:
        t = T.popleft()
        t_pos += 1
        if s == t:
            collect_pos.append(t_pos)
            break

# print(S, T)
print(*collect_pos)