import sys

def main(lines):
    level = []
    step = lines[0]
    ct = 0
    m = 10 ** 8
    N, X, Y = list(map(int, (lines[1].split())))
    for line in lines[2:]:
        low, high = list(map(int, (line.split())))
        level.append(high - low)
    if step == '1':
        print(sum(level))
    if step == '2':
        for y in range(max(level), -1, -1):
            ct = y
            nl = [x - y for x in level]
            for l in nl:
                if l <= 0:
                    continue
                ct += (l + X - 1) // X
        if m > ct:
            m = ct
        print(m)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
