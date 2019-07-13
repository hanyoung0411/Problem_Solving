N = int(input())
first_price = []
second_price = []
for _ in range(N) :
    first_order,second_order = map(int,input().split())
    first_price.append(first_order)
    second_price.append(second_order)
print(min(first_price))
print(min(second_price))
for i in range(N) :
    i
