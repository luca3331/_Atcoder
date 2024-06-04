B = int(input())
a = 1
while pow(a, a) <= B:
    if pow(a, a) == B:
        print(a)
        exit()
    a += 1
print('-1')