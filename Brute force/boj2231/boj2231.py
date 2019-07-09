import sys
def sumofnum (n) :
    value = 0
    while n != 0 :
        value += n % 10
        n = n // 10
    return value

N = int(input())
if N > 55 :
    i = N-55
else :
    i = 0
while i < N :
    if i + sumofnum(i) == N :
        print(i)
        sys.exit(0)
    i = i + 1
print(0)
