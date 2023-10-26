from collections import defaultdict
dict_ = defaultdict(list)
N = int(input())
max_time = 0
for n in range(N):
    T, D = map(int, input().split())
    if max_time < T + D:
        max_time = T + D
    dict_[T].append(T + D)
print(dict_)

for i in range(max_time):
    if i in dict_.keys():
        dict_[i].pop(0)