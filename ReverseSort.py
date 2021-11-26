import sys
input = sys.stdin.readline

N = int(input())

lst = input().split()

lst1 = [int(i) for i in lst]

def bubbleSortCount(lst):
    count = 0
    for i in range(len(lst)-1):
        for y in range(len(lst)-1):
            if lst[y] < lst[y+1]:
                lst[y],lst[y+1] = lst[y+1],lst[y]
                count = count+1
    return count

print(bubbleSortCount(lst1))