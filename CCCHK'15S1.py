#using right and left pointer
n, M = map(int, input().split())
nums = input().split()
nums = [int(i) for i in nums]
nums.sort()
right_pointer = 0 
left_pointer = len(nums) - 1



output = 0

while True:
    if left_pointer < right_pointer:
        break
    
    if nums[right_pointer] + nums[left_pointer] <= M:
        output += (left_pointer - right_pointer)
        right_pointer += 1
    
    elif nums[right_pointer] + nums[left_pointer] > M:
        left_pointer -= 1 

if output < (10**9) + 7:
    print(output)
else:
    print(output%((10**9 + 7)))

