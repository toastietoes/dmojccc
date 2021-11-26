import sys
input = sys.stdin.readline

n = int(input())

boxesList = []



for i in range(n):
    box = input().split()
    box = [int(i) for i in box]
    box.sort()
    boxesList.append(box)

m = int(input())



for i in range(m):
    possibleBoxes = []
    thing = input().split()
    thing = [int(i) for i in thing]
    thing.sort()
    
    
    for i in boxesList:
        if i[0] >= thing[0] and i[1] >= thing[1] and i[2] >= thing[2]:
            possibleBoxes.append(i[0]*i[1]*i[2])
    
    if len(possibleBoxes) == 0:
        print("Item does not fit.")
    
    else:
        print(min(possibleBoxes))
    


    
    




