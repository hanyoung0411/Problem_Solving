N,M = map(int,input().split())
cards = list(map(int,input().split()))
result = -1
for i in range(N) :
    for j in range(i+1,N) :
        for k in range(j+1,N) :
            sum_numbers = cards[i]+cards[j]+cards[k]
            if sum_numbers > result and sum_numbers <= M :
                result = sum_numbers
print(result)
