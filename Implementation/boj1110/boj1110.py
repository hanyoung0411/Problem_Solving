num = int(input())
prior_cmp = num
cnt = 0
cmp = -1
while cmp != num:
    cmp = (prior_cmp//10) + (prior_cmp%10)
    cmp = (prior_cmp%10)*10 + (cmp%10)
    prior_cmp = cmp
    cnt +=1
print(cnt)
