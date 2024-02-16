import math
def isPrime(n):
    if n < 2:
        return 0
    else:
        if n==2 or n==3:
            return 1
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                return 0
        return 1

n, m = map(int, input().split())

for i in range(n):
    a = list(map(int, input().split()))
    for j in a:
        print(isPrime(j), end = ' ')
    print()