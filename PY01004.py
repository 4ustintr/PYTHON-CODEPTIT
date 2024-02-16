import math
n=int(input())
def kt_so_nt(n):
    if n<2:
        return False
    else:
        if n==2 or n==3:
           return True
        else:
            for i in range(2,int(math.sqrt(n))+1,1):
                 if n%i==0:
                    return False
            return True
while n>0:
    t=int(input())
    d=0
    for i in range(t):
        if math.gcd(i,t)==1:
            d+=1
    if kt_so_nt(d)==True:
        print("YES")
    else:
        print("NO")
    n-=1