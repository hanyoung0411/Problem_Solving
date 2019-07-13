def fac (n):
    if n == 1 :
        return 1;
    return n*fac(n-1);

N = int(input());
if N == 0 :
    print(1)
else :
    print(fac(N));
