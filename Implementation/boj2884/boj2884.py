hr,m=map(int,input().split())
if m < 45 :
    if hr == 0 :
        print(23,60-(45-m))
    else :
        print(hr-1,60-(45-m))
else :
    print(hr,m-45)
