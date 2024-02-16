a,k,n=map(int,input().split())
b=k-(a%k)
c=n-a
if b>c:
    print("-1")
else:
    for i in range(b,c+1,k):
        print(i,end=" ")
