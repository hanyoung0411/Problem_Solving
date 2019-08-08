def get_distance(a,b,c,d) :
    return (a-c) ** 2 + (b-d) ** 2

T = int(input())
for _ in range(T) :
    x1,y1,x2,y2 = map(int,input().split())
    planets = []
    n = int(input())
    for _ in range(n) :
        planets.append(list(map(int,input().split())))
    start_planets = []
    arrive_planets = []
    for i in range(n) :
        if get_distance(x1,y1,planets[i][0],planets[i][1]) < planets[i][2] ** 2 :
            start_planets.append(i)
        if get_distance(x2,y2,planets[i][0],planets[i][1]) < planets[i][2] ** 2 :
            arrive_planets.append(i)
        if len(start_planets) > 0 and len(arrive_planets) > 0 :
            if start_planets[-1] == arrive_planets[-1] :
                del start_planets[-1]
                del arrive_planets[-1]
    print(len(start_planets)+len(arrive_planets))
        
    
