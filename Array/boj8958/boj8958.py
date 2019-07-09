from sys import stdin
N = int(stdin.readline())
for _ in range(N) :
    case = stdin.readline()
    result = 0
    cnt = 0
    for i in range(len(case)) :
        if case[i] == 'O' :
            cnt = cnt + 1
        else :
            cnt = 0
        result += cnt
    print(result)
