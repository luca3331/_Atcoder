N = int(input())
W = input().split()
flag = False
for x in W:
    if x == "and" or x == "not" or x == "that" or x == "the" or x == "you":
        flag = True
        print("Yes")
        break
if not flag:
    print("No")