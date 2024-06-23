sx, sy = map(int, input().split())
tx, ty = map(int, input().split())
print(abs(ty - sy) + max(abs(tx - sx) - abs(ty - sy + 1), 0))
