import sys
N = int(sys.stdin.readline())
numbers = []
for _ in range(N) :
    numbers.append(int(sys.stdin.readline()))
numbers.sort()
print(numbers)
for i in range(N) :
    print(numbers[i])
