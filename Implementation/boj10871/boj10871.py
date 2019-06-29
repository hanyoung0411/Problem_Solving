import sys
N,X = map(int,sys.stdin.readline().split())
num = sys.stdin.readline().split()
for i in range(N) :
    if int(num[i]) < X :
        print(num[i],end = " ")
