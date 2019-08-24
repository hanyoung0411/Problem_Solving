import sys
N,M = map(int,sys.stdin.readline().split())
outsider_hear = set()
outsider_see = set()
for _ in range(N) :
    outsider_hear.add(sys.stdin.readline())
for _ in range(M) :
    outsider_see.add(sys.stdin.readline())
outsider = list(outsider_hear & outsider_see)
outsider.sort()
print(len(outsider))
for name in outsider :
    print(name, end='')
