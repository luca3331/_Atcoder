N, X, Y, Z = input().split()
if int(X) <= int(Z) <= int(Y) or int(Y) <= int(Z) <= int(X):
    print("Yes")
else:
    print("No")