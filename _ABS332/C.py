N, M = map(int, input().split())
S = input()
num = [x for x in range(1, N + 1)]
def is_can(v):
    MM, TT = M, v
    for n in range(N):
        if S[n] == '0':
            MM, TT = M, v
        elif S[n] == '1':
            if MM > 0:
                MM -= 1
            elif TT > 0:
                TT -= 1
            else:
                return False
        elif S[n] == '2':
            if TT > 0:
                TT -= 1
            else:
                return False
    return True

def bisect():
    left = 0
    right = N - 1
    while left <= right:
        mid = (left + right) // 2
        if is_can(mid):
            right = mid - 1
        else:
            left = mid + 1
    return left

print(bisect())

