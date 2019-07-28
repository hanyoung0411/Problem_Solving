fib_num = [0]*46
def print_fib(n) :
        if fib_num[n] != 0 :
            return fib_num[n]
        if n == 1 :
            fib_num[1] = 1
            return 1
        elif n == 0 :
            fib_num[0] = 0
            return 0
        else :
            fib_num[n] = print_fib(n-2) + print_fib(n-1)
            return fib_num[n]

K = int(input())
print(print_fib(K-1),print_fib(K))
