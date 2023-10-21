N, D = map(int, input().split())
T = list(map(int, input().split()))
flag = False

for i in range(1, len(T)):
    if T[i] - T[i - 1] <= D:
        flag = True
        time = T[i]

if flag:
    print(time)
else:
    print('-1')