N, V = map(int, input().split())
coins_input = input().split()

for i in range(V):
    cost, coin_position = map(int, input().split())
    least = [-1 for i in range(cost+1)]
    least[0] = 0
    for i in range(len(least)):
        for y in coins_input[:coin_position]:
            if least[i] > -1 and i + int(y) < cost+1:
                if least[i+int(y)] == -1:
                    least[i+int(y)] = least[i]+1
                else:
                    if least[i] + 1 < least[i+int(y)]:
                        least[i+int(y)] = least[i] + 1
    print(least[-1])
                
  

    