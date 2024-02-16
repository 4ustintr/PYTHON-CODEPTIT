n=int(input())
while n>0:
    a=input()
    k=list(a)
    d=0
    for i in range(1,len(k),1):
        if a[i]>=a[i-1]:
            d+=1
    if d==len(k)-1:
       print("YES")
    else:
       print("NO")
    n-=1