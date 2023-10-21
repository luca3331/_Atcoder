N, M = map(int, input().split())
L = list(map(int, input().split()))
LLL = [L[0]]
for l in L[1:]:
    LLL.append(l + LLL[-1] + 1)

min_len = (LLL[-1] + M - 1) // M
max_len = (LLL[-1] - L[-1] + (M - 1) - 1) // (M - 1)


def is_can(v):
    ct = 0
    LL = 0
    for i in range(len(L) - 1):
        LL += L[i] + 1
        if LL - 1 <= v <= LL + L[i + 1]:
            ct += 1
            LL = 0
    if ct < M:
        return True
    else:
        return False

def bin_search():
    left, right = (LLL[-1] + M - 1) // M, (LLL[-1] - L[-1] + (M - 1) - 1) // (M - 1)
    while left <= right:
        mid = left + (right - left) // 2

        if is_can(mid):
            right = mid - 1
        else:
            left = mid + 1
    return right


print(bin_search())