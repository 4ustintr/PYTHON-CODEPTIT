a=int(input())
while a>0:
    n,x,m=map(float,input().split())
    res=0
    while n<m:
        n=n+(n*x*0.01)
        res+=1
    print(res)
    a-=1

