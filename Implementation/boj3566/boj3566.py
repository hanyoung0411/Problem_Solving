big = list(map(int,input().split()))
n = int(input())

def assemble() :
    
    val = [0] * 4
    for i in range(4) :
        if small[i] >= big[i] :
                val[i] = 1
        else :
            cal = big[i] - (small[i] * (big[i] // small[i]))
            if cal > 0 :
                val[i] = (big[i] // small[i]) + 1
            elif cal == 0 :
                val[i] = (big[i] // small[i])
    
    return max(val[0],val[2])*max(val[1],val[3])*small[4]                  
    
result = float('inf')
for _ in range(n) :
    small = list(map(int,input().split()))
    
    get_sum = assemble()
    if result > get_sum :
        result = get_sum
        
    small[0],small[1] = small[1],small[0]
    small[2],small[3] = small[3],small[2]
    
    get_sum = assemble()
    if result > get_sum :
        result = get_sum
        
print(result)

