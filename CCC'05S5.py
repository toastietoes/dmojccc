import sys
import math
t = int(sys.stdin.readline()) #total number of games ever played
scores = []
inversions = 0

for i in range(t):
    scores.append(int(sys.stdin.readline()))

def mergeSort(scores):
    global inversions
    if len(scores) > 1:

        mid = math.floor(len(scores)/2)
        leftscores = scores[:mid]
        rightscores = scores[mid:]

        mergeSort(leftscores)
        mergeSort(rightscores)

        i = j = k = 0

        while i < len(leftscores) and j < len(rightscores):
            if leftscores[i] > rightscores[j]:
                scores[k] = rightscores[j]
                j += 1
                inversions += len(leftscores) -i
            else:
                scores[k] = leftscores[i]
                i += 1 
            k+=1

        while i < len(leftscores):
            scores[k] = leftscores[i]
            i += 1
            k += 1
        
        while j < len(rightscores):
            scores[k] = rightscores[j]
            j+=1
            k+=1

mergeSort(scores)
print("%.2f" % float((inversions + t)/float(t)))    


