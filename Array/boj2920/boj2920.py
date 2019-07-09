from sys import stdin
c_major = stdin.readline().split()
order = 0 #1 asc 2 desc 
for i in range (7) :
    if c_major[i] < c_major[i+1] :
        if order == 2 :
            order = 0
            break
        else :
            order = 1
    elif c_major[i] > c_major[i-1] :
        if order == 1 :
            order = 0
            break
        else :
            order = 2
if order == 0 :
    print("mixed")
elif order == 1 :
    print("ascending")
else :
    print("descending")
