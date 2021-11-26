import sys
input = sys.stdin.readline

N = int(input())

lst1 = input().split()

lst1 = [int(i) for i in lst1]

def BubbleSortCopy(lst):
    lst2 = lst.copy()
    for i in range(len(lst)-1):
        for y in range(len(lst)-1):
            if lst2[y] > lst2[y+1]:
                lst2[y],lst2[y+1] = lst2[y+1],lst2[y]
                lstcopy = lst2.copy()
                print(*lstcopy)
print(*lst1)
BubbleSortCopy(lst1)