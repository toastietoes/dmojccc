c, r = map(int, input().split())
x = 0
y = 0

while True:
    move_x, move_y = map(int, input().split())
    if move_x == 0 and move_y == 0:
        break
    
    if move_x > 0 and move_x + x > c:
        x = c
    elif move_x < 0 and x + move_x < 0:
        x = 0
    else:
        x += move_x
    
    if move_y > 0 and move_y + y > r:
        y = r
    elif move_y < 0 and y + move_y < 0:
        y = 0
    else:
        y += move_y
    
    print(x,y)
    

    

