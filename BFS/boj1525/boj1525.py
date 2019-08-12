import queue
import sys

q = queue.Queue() # save the arrange_ment here 
arrangements = {}

def insert_in_queue(arrangement, index, count) :
    if index == 0 :
        swap(arrangement,index,1,count)
        swap(arrangement,index,3,count)
    elif index == 1:
        swap(arrangement,index,-1,count)
        swap(arrangement,index,1,count)
        swap(arrangement,index,3,count)
    elif index == 2:
        swap(arrangement,index,-1,count)
        swap(arrangement,index,3,count)
    elif index == 3:
        swap(arrangement,index,-3,count)
        swap(arrangement,index,1,count)
        swap(arrangement,index,3,count)
    elif index == 4:
        swap(arrangement,index,-1,count)
        swap(arrangement,index,1,count)
        swap(arrangement,index,-3,count)
        swap(arrangement,index,3,count)
    elif index == 5:
        swap(arrangement,index,-1,count)
        swap(arrangement,index,-3,count)
        swap(arrangement,index,3,count)
    elif index == 6:
        swap(arrangement,index,-3,count)
        swap(arrangement,index,1,count)
    elif index == 7:
        swap(arrangement,index,-1,count)
        swap(arrangement,index,-3,count)
        swap(arrangement,index,1,count)
    else : # index == 8
        swap(arrangement,index,-1,count)
        swap(arrangement,index,-3,count)

def swap(arrangement,index, number, count) :

    global arrangements
    
    tmp = list(arrangement)
    tmp[index],tmp[index+number] = tmp[index+number],tmp[index]
    arrangement = ''.join(tmp)
    
    if arrangements.get(arrangement) == None :
        arrangements[arrangement] = count+1
        q.put([arrangement,count+1])

number_list = []
for _ in range(3) :
    rows = list(input().split())
    for number in rows :
        number_list.append(number)
initial_arrangement = ''.join(number_list)
arrangements = {initial_arrangement: 0}
q.put([initial_arrangement,0])

while not q.empty() :
        current = q.get()
        if current[0] == '123456780' :
            print(current[1])
            sys.exit()
        else :
            insert_in_queue(current[0], current[0].index('0'), current[1])
print(-1)

