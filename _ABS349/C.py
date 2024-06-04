S = input()
T = input()
characters = [chr(i) for i in range(ord('A'), ord('Z')+1)]
pos1, pos2, pos3 = 0, 0, 0
flag = False
for xi, t in enumerate(T):
    if T[0] == t.upper():
        for yi, t in enumerate(T[xi:]):
            if T[1] == t.upper():
                if T[2] == 'X':
                    flag = True
                    break
                else:
                    for zi, t in enumerate(T[yi:]):
                        if T[2] == t.upper():
                            flag = True
                            break
            else:
                break
    else:
        break
if flag:
    print('Yes')
else:
    print('No')


