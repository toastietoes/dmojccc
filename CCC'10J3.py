distance = int(input())
clubs = int(input())
club_d = []
moves = [5281 for i in range(distance+1)]
moves[0] = 0

for i in range(clubs):
    club_distance = int(input())
    club_d.append(club_distance)

for i in range(distance+1):
    for y in club_d:
        if i + y <= distance and moves[i] + 1 < moves[i+y]:
            moves[i+y] = moves[i] + 1

if moves[-1] != 5281:
    print("Roberta wins in", moves[-1], "strokes.")
else:
    print("Roberta acknowledges defeat.")