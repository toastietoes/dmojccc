import sys
input = sys.stdin.readline

while True:
    r = int(input())
    
    if r == 0:
        break

    square = (2*r+1)**2
    count = 0
   
    for yPoint in range(1,r+1):
        xcoord = r
        
        for y in range(r):
            
            if (yPoint)**2+(xcoord)**2 > r**2:
                count = count+1
                xcoord = xcoord-1
                
            
            else:
                break
        
    count = count*4
    pennies = square-count
    print(pennies)






    


