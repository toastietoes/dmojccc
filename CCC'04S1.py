N = int(input())
for i in range(N):
    word1 = input()
    word2 = input()
    word3 = input()
    fixfree = True
    
    if len(word1) <= len(word2):
        if word1 == word2[:len(word1)]:
            fixfree = False
        elif word1 == word2[-len(word1):]:
            fixfree = False
    if len(word1) <= len(word3):
        if word1 == word3[:len(word1)]:
            fixfree = False
        elif word1 == word3[-len(word1):]:
            fixfree = False
    
    if len(word2) <= len(word1):
        if word2 == word1[:len(word2)]:
            fixfree = False
        elif word2 == word1[-len(word2):]:
            fixfree = False
    if len(word2) <= len(word3):
        if word2 == word3[:len(word2)]:
            fixfree = False
        elif word2 == word3[-len(word2):]:
            fixfree = False
    
    if len(word3) <= len(word1):
        if word3 == word1[:len(word3)]:
            fixfree = False
        elif word3 == word1[-len(word3):]:
            fixfree = False
    if len(word3) <= len(word2):
        if word3 == word2[:len(word3)]:
            fixfree = False
        elif word3 == word2[-len(word3):]:
            fixfree = False
    if fixfree == True:
        print('Yes')
    else:
        print('No')
    

