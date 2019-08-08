import sys

def traverse(current_loc,visited_vertex) :
    
    if visited_vertex == all_vertex and current_loc == 0 :
        for j in range(len(result)) :
            print(result[j]+1,end=' ')
        sys.exit()
            
    if visited_vertex == all_vertex :
        return
    
    for i in range(N) :
        if current_loc == i :
            continue
        elif vertex[current_loc][i] > 0  :
            vertex[current_loc][i] -= 1
            vertex[i][current_loc] -= 1
            visited_vertex += 2
            result.append(i)
            
            traverse(i,visited_vertex)
            
            vertex[current_loc][i] += 1
            vertex[i][current_loc] += 1
            visited_vertex -= 2
            if len(result) != 0 :
                del result[-1]
    return


N = int(input())
vertex = []
for _ in range(N) :
    vertex.append(list(map(int,input().split())))
    
result = []
all_vertex = 0
flag = 0

for i in range(N):
    all_vertex += sum(vertex[i])
    if sum(vertex[i]) % 2 == 1 :
        flag = 1
if all_vertex == 0 :
    flag = 1
if flag == 0 :        
        result.append(0)
        traverse(0,0)
print(-1)
