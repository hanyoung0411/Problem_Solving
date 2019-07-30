numbers = []
sum_numbers = 0
for i in range(9) :
    numbers.append(int(input()))
    sum_numbers += numbers[i]
    
for i in range(9) :
    for j in range(i+1,9) :
        if sum_numbers - (numbers[i] + numbers[j]) == 100 :
            for k in range(9) :
                if k != i and k != j :
                    print(numbers[k])
            exit(0)

