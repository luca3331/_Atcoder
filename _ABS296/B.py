for i in range(1, 9):
    tmp = input()
    if '*' in tmp:
        print("{}{}".format(chr(97 + tmp.find('*')), 9 - i))