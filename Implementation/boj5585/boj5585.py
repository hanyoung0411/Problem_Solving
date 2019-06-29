#boj5585
#HanYoung 20190628
cost = int(input())
change = 1000 - cost
cnt = 0
change_list = [500,100,50,10,5,1]
for i in range(6) :
    cnt += change // change_list[i]
    change = change - change_list[i]* (change // change_list[i])
print(cnt)