from collections import deque
N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))
A_diff = [-1 for _ in range(N + 1)]
for i in range(N + 1):
    if i == 0:
        A_diff[0] = A[0]
    elif i == N:
        A_diff[i] = L - A[-1]
    else:
        A_diff[i] = A[i] - A[i - 1]

def is_can(score):
    AA = deque(A_diff[:])

    tmp_score = 0
    ct = 0
    while len(AA):
        tmp_score += AA.popleft()
        if tmp_score >= score:
            tmp_score = 0
            ct += 1
        if ct >= K + 1:
            return True
    else:
        return False

def bin_search():
    left = 1
    right = L
    while left <= right:
        mid = (left + right) // 2
        if is_can(mid):
            left = mid + 1
        else:
            right = mid - 1
    return right

print(bin_search())