input()
times = sorted(list(map(int,input().split())))
print(sum([ times[len(times)-i] * i for i in range(len(times),0,-1)]))
