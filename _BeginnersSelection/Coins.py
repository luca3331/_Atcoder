_a = int(input())
_b = int(input())
_c = int(input())
_x = int(input())
count = 0
for a in range(_a + 1):
    for b in range(_b + 1):
        for c in range(_c + 1):
            if 500 * a + 100 * b + 50 * c == _x:
                count = count + 1
print(count)