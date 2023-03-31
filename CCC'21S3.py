N = int(input())
friends = []
max = 0
min = 1000000000000

def getScore(n):
    total = 0
    for i in friends:
        distance =  abs(n-i[0])-i[2]
        if distance > 0:
            total += distance*i[1]
    
    return total

for i in range(N):
    P, W, D = map(int, input().split())
    friends.append([P,W,D])
    if P > max:
        max = P

    if P < min:
        min = P

if len(friends) == 1:
    print(friends[0][0])
else:
    while min < max:
        mid = int((min+max)/2)
        score = getScore(mid)
        left_score = getScore(mid-1)
        right_score = getScore(mid+1)
        
        
        if score < left_score and score < right_score:
            print(score)
            break

        elif score == left_score and score == right_score:
            print(score)
            break
        
        if score < left_score:
            min = mid+1
        elif score < right_score:
            max = mid - 1 


    





