n = int(input())
inpt = list(map(int, input().split()))
calls = []
for i in range(n):
    calls.append([i + 1, inpt[i]])

remain = []

for call in calls:
    index = call[0]
    order = call[1]
    if order != -1:
        calls[order - 1][1] = -1
for call in calls:
    if call[1] != -1:
        remain.append(call[0])
remain = sorted(remain)
print(len(remain))
for i in remain:
    print("{} ".format(i), end="")
