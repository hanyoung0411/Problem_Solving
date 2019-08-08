N = int(input())
for i in range(1,N) :
    number = list(map(int,list(str(i))))
    if i + sum(number) == N :
        result = i
        break
print(result)
