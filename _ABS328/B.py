N = int(input())
D = list(map(int, input().split()))
count = []
for m in range(1, N + 1):
    num = list(str(m))[0]
    if not all([i == num for i in list(str(m))]):
        continue
    for d in range(1, D[m-1] + 1):
        if not all([j == num for j in list(str(d))]):
            continue
        else:
            count.append(tuple([m,d]))
print(len(count))