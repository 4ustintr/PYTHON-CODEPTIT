import math
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
n=int(input())
while n>0:
    a,b=map(int,input().split())
    k=math.gcd(a,b)
    s=0
    while k>0:
        du=k%10
        s=s+du
        k//=10
    if kt_so_nt(s)==True:
        print("YES")
    else:
        print("NO")
    n-=1
