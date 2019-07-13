N = int(input())
scores = list(map(int,input().split()))
print(sum(scores)/len(scores)/max(scores)*100)
