import math
def digitsum(n):
    n = int(1 << n) #2^n
    S = 0
    while n > 1 :
        S += math.floor((n%10))
        n /= 10
        print(n)
        print(n %10)
    return S


print(digitsum(1000));
