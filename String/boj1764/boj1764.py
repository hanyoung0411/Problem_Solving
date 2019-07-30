import sys
N,M = map(int,sys.stdin.readline().split())
outsider_hear = []
result = []
for _ in range(N) :
    outsider_hear.append(sys.stdin.readline())
    
for _ in range(M) :
    outsider_see = sys.stdin.readline()
    if outsider_hear.find(outsider_see) :
        result.append(outsider_see)
result.sort()
for i in range(len(result)) :
    print(result[i],end=' ')
