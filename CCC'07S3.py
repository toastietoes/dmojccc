#every student gets a friend
#friendship is one-way ex Janet -> Sarah 
#circle of friends can occur
#seperation of 0 if friends, seperation of 1 if friend of friend, so on...
#determing if two friends are in same circle and their seperation

from collections import deque

n = int(input())
friends = {}

for i in range(n):
    x, y = map(int, input().split())
    if x not in friends:
        friends[x] = [y]
    else:
        friends[x].append(y)


while True:
    distance = 0 
    f1, f2 = map(int, input().split())
    
    if f1 == 0:
        break 
    
    queue = deque([f1])
    visited = [f1]

    while len(queue) != 0:
        check = queue.popleft()
        if check in friends:
            if f2 in friends[check]:
                visited.append(f2)
                break
            elif visited.count(check) == 2:
                break
            else:
                for i in friends[check]:
                    queue.append(i)
                    visited.append(i)
                    distance += 1
    
    if f2 in visited:
        print('Yes', distance)
    else:
        print('No')






    
