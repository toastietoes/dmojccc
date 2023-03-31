t = int(input())

for i in range(t):
    w, h = input().split() 
    if int(w)*int(h)%2 == 0:
        print('good')
    else:
        print('bad')
