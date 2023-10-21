N = int(input())
ct = 0
for i in range(1, N + 1):
    digits = len(list(str(i)))
    if digits % 2 == 1:
        ct += 1
print(ct)