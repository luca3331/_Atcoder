from collections import defaultdict
SS = input()
TT = input()

g1 = set([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('A', 'E')])
g2 = set([('A', 'C'), ('A', 'D'), ('B', 'D'), ('B', 'E'), ('C', 'E')])

bool1 = tuple(sorted((SS[0], SS[1]))) in g1
bool2 = tuple(sorted((TT[0], TT[1]))) in g1
if bool1 == bool2:
    print('Yes')
else:
    print('No')

