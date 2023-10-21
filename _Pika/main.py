import sys


def main(lines):
    # 入力のパース
    step = int(lines[0])
    N, X, Y = map(int, lines[1].split())
    level = []
    for line in lines[2:]:
        low, high = map(int, line.split())
        level.append(high - low)

    # ステップ1の場合
    if step == 1:
        ans = sum(level)
        print(ans)
        return

    # ステップ2の場合
    # 2分探索の初期化
    left, right = 0, max(level)
    while left < right:
        mid = (left + right + 1) // 2  # 2分探索の中央値
        cnt = 0  # 必要なレベルアップ回数の合計
        cur_level = N  # 現在のレベル
        for i in range(N):  # 各モンスターに対して
            if level[i] >= mid:  # Y匹ずつレベルアップする場合
                cnt += (level[i] - mid) // Y + 1  # 必要な回数を加算
                cur_level += (level[i] - mid) // Y * X  # レベルアップ
            else:  # Xで一気にレベルアップする場合
                need_x = mid - level[i]  # 必要なレベルアップ回数
                cnt += 1  # 必要な回数を加算
                cur_level += need_x * X  # レベルアップ
            if cnt > i + 1:  # 必要な回数がN(i)を超えた場合
                break
        if cnt <= N:  # 必要な回数がN匹以下に収まった場合
            right = mid - 1  # Yの値を減らす
        else:
            left = mid  # Yの値を増やす
    ans = left
    for l in level:
        if l >= left:
            ans += (l - left) // X + 1
    print(ans)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
