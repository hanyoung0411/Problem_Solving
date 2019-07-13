remainder = [0]*42
for _ in range(10) :
    num = int(input())
    remainder[num % 42] = 1
print(42 - remainder.count(0))
    
