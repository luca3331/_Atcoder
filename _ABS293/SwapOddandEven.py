s = list(input())
out = ""
while len(s) > 1:
    out += s.pop(1) + s.pop(0)
if len(s) == 1:
    out += s.pop()
print(out)