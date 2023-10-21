P = [input() for _ in range(12)]
A = P[:4]
B = P[4:8]
C = P[8:12]

A_coords = []
B_coords = []
C_coords = []
for r in range(4):
    for c in range(4):
        if A[r][c] == '#':
            A_coords.append((r, c))
        if B[r][c] == '#':
            B_coords.append((r, c))
        if C[r][c] == '#':
            C_coords.append((r, c))

def get_dimensions(tetromino):
    """
    テトリスミノの縦幅と横幅を求める関数
    :param tetromino: テトリスミノを表す座標のリスト
    :return: 縦幅と横幅のタプル
    """
    if not tetromino:
        return 0, 0

    # ミノのx座標とy座標をそれぞれ別々のリストに分ける
    y_coords, x_coords = zip(*tetromino)

    # 縦幅と横幅を計算
    height = max(y_coords) - min(y_coords) + 1
    width = max(x_coords) - min(x_coords) + 1

    return height, width

def rotate_tetromino(tetromino):
    """
    テトリスミノを90度時計回りに回転させる関数
    :param tetromino: テトリスミノを表す座標のリスト
    :return: 回転後のテトリスミノの座標のリスト
    """
    rotated_tetromino = [(y, -x) for x, y in tetromino]
    return rotated_tetromino

def append_cands(tetromino):
    cands = [[tetromino]]
    while True:
        for mino in tetromino:
            

A_h, A_w = get_dimensions(A_coords)
B_h, B_w = get_dimensions(B_coords)
C_h, C_w = get_dimensions(C_coords)

A_cands = []
B_cands = []
C_cands = []
tmp = rotate_tetromino(A_coords)
print(A, B, C)
