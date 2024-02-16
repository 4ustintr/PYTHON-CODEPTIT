t=int(input())
def sum_list(n):
    s=0
    while n>0:
        s+=(n%10)
        n//=10
    return s
while t>0:
    t-=1
    n=int(input())
    a=list(map(int,input().split()))
    k=[]
    b={}
    for i in range(len(a)):
        k.append(sum_list(a[i]))
    for i in range(len(a)):
        b[a[i]]=k[i]
    values=sorted(b.values())
    for value in values:
       key = b.keys()[values.index(value)]
       print(key)
    
    
    

