num_len = int(input())
num_list = list(map(int, input().split()))
count = 0


def div2(ele):
    return ele / 2


while True:
    for ele in num_list:
        if ele % 2 == 1:
            print(count)
            exit()
            break
    num_list = list(map(div2,num_list))
    count = count + 1
