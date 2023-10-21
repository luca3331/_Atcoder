s = input()
words = ""
tmp = ""

while True:
    if s[-5:] == "dream" or s[-5:] == "erase":
        s = s[:-5]
    elif s[-6:] == "eraser":
        s = s[:-6]
    elif s[-7:] == "dreamer":
        s = s[:-7]
    elif len(s) == 0:
        print("YES")
        break
    else:
        print("NO")
        break

#
#
# def is_equal(elements, ignore_str_len):
#     for index, char in reversed(list(enumerate(elements[:len(elements) - ignore_str_len]))):
#         if len(elements) <= index:
#             break
#         if char != string[-(len(elements) - index)]:
#             return False
#     return True
#
#
# while True:
#     for ele in str_list:
#         tmp = ele + words
#         if is_equal(tmp, len(words)):
#             words = tmp
#             break
#         else:
#             tmp = words
#     if words == string:
#         flag = True
#         break
#     if len(words) == 0:
#         break
#     if len(string) < len(words):
#         break
#
# if flag:
#     print("YES")
# else:
#     print("NO")