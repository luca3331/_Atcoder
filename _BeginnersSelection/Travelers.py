num = int(input())
schedules = []
flag = True
for index in range(num):
    time, x, y = map(int, input().split())
    schedules.append([time, x, y])
time, x, y = 0, 0, 0
for schedule in schedules:
    time_buff = schedule[0] - time
    x_delta = abs(schedule[1] - x)
    y_delta = abs(schedule[2] - y)
    if x_delta + y_delta > time_buff or (time_buff % 2 != x_delta + y_delta % 2):
        flag = False
    time = schedule[0]
    x = schedule[1]
    y = schedule[2]
if flag:
    print("Yes")
else:
    print("No")