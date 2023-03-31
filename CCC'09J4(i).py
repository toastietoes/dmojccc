from collections import deque

w = int(input())

w1 = 'WELCOME'
w2 = 'TO'
w3 = 'CCC'
w4 = 'GOOD'
w5 = 'LUCK'
w6 = 'TODAY'

words = deque([w1, w2, w3, w4, w5, w6])



line_output = []

print(len(words))

while len(words) > 0:
    char_count = 0
    print(words)
    line = []
    
    while True:
        if len(words) > 0:
            word = words[0] 
            if char_count + len(word) <= w and len(line) == 0:
                char_count += (len(word))
                words.popleft()
                line.append([word])
            elif char_count + len(word) + 1 <= w and len(line) > 0:
                char_count += len(word) + 1
                line.append(['.'+word])
                words.popleft()
            else:
                break
        else:
            break
    
    print(line)
    
    while True:
        for i in range(1, len(line)):
            if char_count + 1 <= w:
                line[i] = ['.' + line[i][0]] 
                char_count += 1
            else:
                line_output.append(line)
                break
        if char_count + 1 > w:
            break
    print(line_output)

print(line_output)










