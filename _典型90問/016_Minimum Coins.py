N = int(input())
ABC = sorted(list(map(int, input().split())))
# A < B < Cとする
A, B, C = ABC
N_div_C = N // C
for n_div_c in reversed(range(1, N // C + 1)):
    N_C = N - (n_div_c * C)
    for n_div_b in reversed(range(1, N_C // B + 1)):
        N_B = N_C - (n_div_b * B)
        for n_div_a in reversed(range(1, N_B // A + 1)):
            N_A = N_B - (n_div_a * A)
            if N_A == 0:
                print(n_div_c + n_div_b + n_div_a)
                break