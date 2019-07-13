A = int(input())
B = int(input())
C = int(input())
num = str(A * B * C)
numbers = [0]*10
for i in range(len(num)) :
    numbers[int(num[i])] += 1
for i in range(10) :
    print(numbers[i])
