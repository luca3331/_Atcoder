num = input()
cards = sorted(list(map(int, input().split())), reverse=True)
Bob = 0
Alice = 0
for index, ele in enumerate(cards):
    if index % 2 == 0:
        Alice += ele
    else:
        Bob += ele
print(Alice - Bob)
