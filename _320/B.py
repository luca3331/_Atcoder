S = input()

def is_can(mid):
    for i in range(0, len(S) - mid + 1):
        div = mid + (2 - mid)
        if mid % 2 == 1:
            front = list(S[i:mid // 2 + i + 1])
            back = list(S[i + mid // 2:i + mid // 2 + mid // 2 + 1])
            back.reverse()
            if front == back:
                return True
            else:
                continue
        else:
            front = list(S[i:mid // 2 + i])
            back = list(S[i + mid // 2: i + mid // 2 + mid // 2])
            back.reverse()
            if front == back:
                return True
            else:
                continue
    return False


def search():
    _max = 0
    for i in range(1, len(S) + 1):
        if is_can(i):
            _max = i
    print(_max)

search()