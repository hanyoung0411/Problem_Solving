
stars = []

def store_star(start_point,size) :
    if size == 3 :
        for i in range(3) :
            for j in range(3) :
                if i == 1 and j == 1 :
                    continue
                else :
                    stars[start_point[0]+i][start_point[1]+j] = 1
        return
    else :
        for i in range(3) :
            for j in range(3) :
                if i == 1 and j == 1 :
                    continue
                else :
                    store_star([start_point[0]+i*(size//3),start_point[1]+j*(size//3)],(size//3))

N = int(input())
stars = [[0 for _ in range(N)] for _ in range(N)]
store_star([0,0],N)
for i in range(N) :
    for j in range(N) :
        if stars[i][j] == 1 :
            print('*',end='')
        else :
            print(' ',end='')
    print()
