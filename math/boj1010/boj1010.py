import math
def combination(n,r) :
    f = math.factorial
    return f(n) // f(r) // f(n-r)

T = int(input())
for _ in range(T) :
    N,M = map(int,input().split())
    print(combination(M,N))
    
