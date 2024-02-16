t=int(input())
while t>0:
    t-=1
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=[]
    k=max(a)
    for i in range(len(a)):
        if a[i]==k:
            a.insert(i-1,m)
            break
    for i in range(len(a)):
        if a[i]<0:
            b.append(a[i])
    for i in range(len(a)):
        if a[i]>=0:
            b.append(a[i])
    for i in b:
        print(i,end=" ")