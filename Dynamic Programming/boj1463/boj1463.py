N = int(input())
level = 0
computed_val = []
level_val = []
level_val.append(N)

while (1 in level_val) != True :
    current_val = []
    for num in level_val :
        if not (num in computed_val) :
            if num % 3 == 0 :
                current_val.append(num // 3)
            if num % 2 == 0 :
                current_val.append(num // 2)
            current_val.append(num - 1)
    level_val = list(set(current_val))
    computed_val.append(level_val)
    level += 1
print(level)
    
