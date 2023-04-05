target = int(input())
width = int(input())
xcoord = int(input())
coord = []

def recurse(level, width, x1, y1, x2, y2):
    global coord
    global target
    
    if level == -1:
        return coord
    
    distance = int(width/3)
    
    if y1 == y2:
    
        set1 = [(x1,y1), (x1+distance,y1)]
        if xcoord >= x1 and xcoord <= x1+distance and level == 0:
            if y1 not in coord:
                coord.append(y1)
        set2 = [(x1+distance, y1), (x1+distance,y1+distance)]
        if xcoord == x1+distance and level == 0:
            if y1 not in coord:
                coord.append(y1)
            if y1+distance not in coord:
                coord.append(y1+distance)
        set3 = [(x1+distance, y1+distance), (x1+distance*2, y1+distance)]
        if xcoord >= x1+distance and xcoord <= x1+distance*2 and level == 0:
            if y1+distance not in coord:
                coord.append(y1+distance)
        set4 = [(x1+distance*2, y1+distance), (x1+distance*2, y1)]
        if xcoord == x1+distance*2 and level == 0:
            if y1+distance not in coord:
                coord.append(y1+distance)
            if y1 not in coord:
                coord.append(y1)
        set5 = [(x1+distance*2, y1), (x1+distance*3, y1)] 
        if xcoord >= x1+distance*2 and xcoord <= x1+distance*3 and level == 0:
            if y1 not in coord:
                coord.append(y1)
        
    elif y2 < y1:
        set1= [(x1,y1), (x1, y1-distance)]
        if xcoord == x1 and level == 0:
            if y1 not in coord:
                coord.append(y1)
            if y1-distance not in coord:
                coord.append(y1-distance)
        set2 = [(x1, y1-distance), (x1+distance, y1-distance)]
        if xcoord >= x1 and xcoord <= x1+distance and level == 0:
            if y1-distance not in coord:
                coord.append(y1-distance)
        set3 = [(x1+distance, y1-distance), (x1+distance, y1-distance*2)]
        if xcoord == x1+distance and level == 0:
            if y1-distance not in coord:
                coord.append(y1-distance)
            if y1-distance*2 not in coord:
                coord.append(y1-distance*2)
        set4 = [(x1+distance, y1-distance*2), (x1, y1-distance*2)]
        if xcoord >= x1 and xcoord <= x1+distance and level == 0:
            if y1-distance*2 not in coord:
                coord.append(y1-distance*2)
        set5 = [(x1, y1-distance*2), (x1, y1-distance*3)]
        if xcoord == x1 and level == 0:
            if y1-distance*2 not in coord:
                coord.append(y1-distance*2)
            if y1-distance*3 not in coord:
                coord.append(y1-distance*3)
    elif y2 > y1:
        set1 = [(x1,y1), (x1,y1+distance)]
        if xcoord == x1 and level == 0:
            if y1 not in coord:
                coord.append(y1)
            if y1+distance not in coord:
                coord.append(y1+distance)
        set2 = [(x1,y1+distance), (x1-distance, y1+distance)]
        if xcoord <= x1 and xcoord >= x1 - distance and level == 0:
            if y1+distance not in coord:
                coord.append(y1+distance)
        set3 = [(x1-distance, y1+distance), (x1-distance, y1+distance*2)]
        if x1-distance == xcoord and level == 0:
            if y1+distance not in coord:
                coord.append(y1+distance)
            if y1+distance*2 not in coord:
                coord.append(y1+distance*2)
        set4 = [(x1-distance, y1+distance*2), (x1, y1+distance*2)]
        if xcoord >= x1 - distance and xcoord <= x1 and level == 0:
            if y1+distance*2 not in coord:
                coord.append(y1+distance*2)
        set5 = [(x1, y1+distance*2), (x1, y1+distance*3)]
        if x1 == xcoord and level == 0:
            if y1+distance*2 not in coord:
                coord.append(y1+distance*2)
            if y1+distance*3 not in coord:
                coord.append(y1+distance*3)
    recurse(level-1, distance, set1[0][0], set1[0][1], set1[1][0], set1[1][1])
    recurse(level-1, distance, set2[0][0], set2[0][1], set2[1][0], set2[1][1])
    recurse(level-1, distance, set3[0][0], set3[0][1], set3[1][0], set3[1][1])
    recurse(level-1, distance, set4[0][0], set4[0][1], set4[1][0], set4[1][1])
    recurse(level-1, distance, set5[0][0], set5[0][1], set5[1][0], set5[1][1])
recurse(target,width,0,1,width,1)
coord.sort()
print(coord)
