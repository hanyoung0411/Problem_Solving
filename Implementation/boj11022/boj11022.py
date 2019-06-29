import sys
N = int(input())
for i in range(N) :
    x,y = map(int,sys.stdin.readline().split())
    print("Case #"+str(i+1)+":",x,"+",y,"=",x+y)
