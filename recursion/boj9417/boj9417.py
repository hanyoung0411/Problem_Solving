import sys
def gcd(a,b) :
    if b == 0 :
        return a
    return gcd(b, a % b)

a,b = map(int,input().split())
gcd_val = gcd(a,b)
print(gcd_val)
print(a * b // gcd_val)
