H, W = map(int, input().split())
board = [list(input().split()) for _ in range(H)]
ct = 0
looted = set()


def expl(x, y):
    global ct
    if board[y][x] in looted:
        return
    if y == H - 1 and x == W - 1:
        ct += 1
        return
    else:
        looted.add(board[y][x])
        if y + 1 < H:
            expl(x, y + 1)
        if x + 1 < W:
            expl(x + 1, y)
    looted.remove(board[y][x])


expl(0, 0)
print(ct)
