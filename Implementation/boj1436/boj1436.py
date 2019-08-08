N = int(input())
number = 666
start = 0
while start != N :
    if str(number).count('6') >= 3 and '666' in str(number) :
        start += 1
    number += 1
    
print(number-1)

'''
666
1666
2666
3666
4666
5666
6660
6661
6662
6663
6664
6665
6666
6667
6668
6669
7666
8666
9666
10666
'''
