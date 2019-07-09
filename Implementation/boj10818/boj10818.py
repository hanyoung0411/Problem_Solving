import sys
while True :
    try :
        num_list.append(int(sys.stdin.readline()))
    except :
        N = max(num_list)
        print(N)
        print(num_list.index(N)+1)
        break
