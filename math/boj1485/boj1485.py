import math

def get_length(x1,y1,x2,y2) :
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

N = int(input())
for _ in range(N) :
    location = []
    for i in range(4):
        location.append(list(map(int,input().split())))
        
    length = []
    for i in range(4) :
        for j in range(i+1,4) :
            length.append(get_length(location[i][0],location[i][1],location[j][0],location[j][1]))
    length.sort()

    result = 1
    for i in range(1,4) :
        if length[0] != length[i] :
            result = 0
    if result == 1 and length[4] == length[5] :
        result = 1
    else : 
        result = 0
    print(result)
