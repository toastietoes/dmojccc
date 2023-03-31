N = int(input())
circle = ['M']*N

for i in range(N):
    if i > 0:
        if circle[i-1] == 'M' and circle[i-1] == 'M':
            circle[i-1] = '_'  

print(circle)

