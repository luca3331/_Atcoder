from itertools import product
N = int(input())
repunit_list = ['1', '11', '111']
repunit_digit = 3
while True:
    if len(set(list(product(repunit_list, repeat=3)))) < N:
        repunit_digit += 1
        repunit = ''
        for n in range(repunit_digit):
            repunit += '1'
        repunit_list.append(repunit)
    else:
        # elements = sorted(set(tuple(sorted(list(product(repunit_list, repeat=3))))), key=lambda x: sum(map(int, x)))
        elements = list(product(repunit_list, repeat=3))
        cand = set([])
        for ele in elements:
            ele = sorted(map(int, ele))
            if ele not in cand:
                cand.add(list(ele))
            if len(cand) == N:
                print(sum(map(int, ele)))
                exit()