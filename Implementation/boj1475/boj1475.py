N = input()
a = []
for i in range(11) :
    a.append(0)
for num in N :
    a[int(num)] +=1
num_sum = a[6]+a[9]
a[9] = -1
if num_sum % 2 == 0 :
    a[6] = num_sum/2
else :
    a[6] = num_sum/2+1
print(int(max(a)))
