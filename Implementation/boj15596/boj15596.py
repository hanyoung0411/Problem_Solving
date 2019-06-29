n = int(input())
x = map(int,input().split())
print(x)
def solve(a):
    ans = 0
    for i in range(len(a)) :
        ans += num_list[i]
    return ans
print(solve(x))
