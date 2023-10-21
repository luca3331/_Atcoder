A, B = map(int, input().split())

def gcd(a, b, c):
    if b == 0:
        return c - 1
    else:
        return gcd(b, a % b, c + a // b)

print(gcd(A, B, 0))
