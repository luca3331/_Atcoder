S = input()
i = 0
ct = 0
max_ct = 0
while i < len(S):
    if S[i] == 'A' or S[i] == 'C' or S[i] == 'T' or S[i] == 'G':
        ct += 1
    else:
        ct = 0
    if max_ct < ct:
        max_ct = ct
    i += 1
print(max_ct)