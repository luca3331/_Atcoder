import numpy as np
N, D = map(int, input().split())
W = sorted(list(map(int, input().split())), reverse=True)
bag = [0] * D
for d in range(D):
    bag[d] = W[d]
for w in W[D:]:
    bag[bag.index(min(bag))] += w
# print(bag)
mean = sum(bag) / D
print( sum( [(x - mean)**2 for x in bag] ) / D)
# print(np.var(bag))