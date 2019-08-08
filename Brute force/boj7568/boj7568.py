N = int(input())
people = []
result = [0]*N
for _ in range(N) :
    people.append(list(map(int,input().split())))
for i in range(N) :
    for j in range(N) :
        if i == j :
            continue;
        if people[i][0] < people[j][0] and people[i][1] < people[j][1] :
            result[i] +=1
for i in range(N) :
    print(rank[i]+1,end = ' ')
