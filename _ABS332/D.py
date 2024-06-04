import numpy as np
H, W = map(int, input().split())
A = [input().split() for _ in range(H)]
B = [input().split() for _ in range(H)]
print(A, B)

def is_can(v):
    vv = v
    for h in range(H):
        for w in range(W):
            if

def bisect():
    left = 0
    right = H * W
    while left <= right:
        mid = (left + right) // 2
        if is_can(mid):
            right = mid - 1
        else:
            left = mid + 1
    return left

print(bisect())

