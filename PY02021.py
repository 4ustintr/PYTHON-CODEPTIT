t=int(input())
while t>0:
    t-=1
    n,m,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    d=0
    k=[]
    for i in a:
        if i in b and i in c:
            print(i,end=" ")
            d+=1
    if d==0:
        print("NO")
