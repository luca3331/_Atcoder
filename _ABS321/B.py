import copy

N, X = map(int, input().split())
A = list(map(int, input().split()))
A = sorted(A)
A_copy = copy.deepcopy(A)
A_copy.append(0)
A_copy.remove(max(A))
A_copy.remove(min(A))
want = X - sum(A_copy)
if want >= X:
    print('0')
else:
    A.remove(max(A))
    A.remove(min(A))
    want = X - sum(A)
    if 100 < want:
        print('-1')
    else:
        print(want)

# AA = A[1: len(A) - 1]
# A.append(0)
# AA_ = A
# AA_ = AA_[1: len(AA_) - 1]
# want = X - sum(AA)
# # print(AA)
# if sum(AA_) >= want: # これ以上スコアは不要
#     print('0')
# elif 100 < want: # 不可
#     print('-1')
# else:
#     print(want)
def is_can(mid):



left = 100
right = 0
while left <= right:
    mid = (left + right) // 2
    if is_can(mid):
        right = mid - 1
    else:
        left = mid + 1
if right

left, right = (LLL[-1] + M - 1) // M, (LLL[-1] - L[-1] + (M - 1) - 1) // (M - 1)
while left <= right:
    mid = left + (right - left) // 2

    if is_can(mid):
        right = mid - 1
    else:
        left = mid + 1
return right
