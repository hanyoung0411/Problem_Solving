N,M = map(int,input().split())

board = []
for i in range(N) :
    board.append(input())

pattern1 = []
pattern2 = []
for i in range(8) :
    if i % 2 == 0 :
        pattern1.append('WB'*4)
        pattern2.append('BW'*4)
    else :
        pattern1.append('BW'*4)
        pattern2.append('WB'*4)

result = N*M+1
for i in range(N-7):
    for j in range(M-7):
        cnt_pattern1 = 0
        cnt_pattern2 = 0
        for p in range(8) :
            for q in range(8) :
                if pattern1[p][q] != board[i+p][j+q] :
                    cnt_pattern1 += 1
                if pattern2[p][q] != board[i+p][j+q] :
                    cnt_pattern2 += 1
        if result > cnt_pattern1 :
            result = cnt_pattern1
        if result > cnt_pattern2 :
            result = cnt_pattern2
print(result)
