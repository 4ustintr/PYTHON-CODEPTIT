t=int(input())
while t>0:
    t-=1
    n,d=map(int,input().split())
    a=list(map(int,input().split()))
    b=[]
    s=""
    s1=""
    for i in range(0,d):
        s+=str(a[i])
        s+=" "
    for i in range(d,len(a)):
        s1+=str(a[i])
        if i<len(a)-1:
            s1+=" "
    print(s1,s)