import sys
N = int(sys.stdin.readline())
numbers = {}
result = float('inf')
max_val = -1*float('inf')
for _ in range(N) :
    num = int(sys.stdin.readline())
    if numbers.get(num) == None :
        numbers[num] = 1
        if result == float('inf') :
            result = num
    else :
        numbers[num] += 1
        if numbers[num] == max_val and result > num :
            result = num
        elif numbers[num] > max_val :
            max_val = numbers[num]
            result = num

print(result)
