import sys
N,M = map(int,sys.stdin.readline().split())
array = []
for _ in range(N) :
    array.append(list(map(int,sys.stdin.readline().split())))
M = int(input())
for _ in range(M) :
    i,j,x,y = map(int,sys.stdin.readline().split())
    result = 0
    for m in range(i-1,x):
            result += sum(array[m][j-1:y])
    print(result)
