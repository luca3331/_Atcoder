from collections import deque
N = int(input())
A = list(map(int, input().split()))
# balls = [2 ** a for a in A]
que = deque()

for n in range(N):
    que.append(A[n])
    while True:
        if len(que) <= 1:
            break
        elif que[-1] != que[-2]:
            break
        else:
            new_ball = que[-1] + 1
            que.pop()
            que.pop()
            que.append(new_ball)
# print(A, que)
print(len(que))