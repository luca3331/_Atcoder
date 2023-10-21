N = int(input())
A = map(int, input().split())
out = ""
for a in A:
    if a % 2 == 0:
        out += str(a) + " "
print(out)