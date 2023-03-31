from collections import deque
x = int(input())
y = int(input())

output = [[x]]
last_step = 'left'
index = 0
rotation = 1
count = 0

for i in range(x+1,y+1):
    if last_step == 'left':
        output.append([i])
        count += 1
        if count == rotation:
            count = 0
            last_step = 'down'
    if last_step == 'down':
        output[index+1].append(i)
        count += 1
        if count == rotation:
            last_step = 'right'
    if last_step == 'right':
        output[index].append(i)



