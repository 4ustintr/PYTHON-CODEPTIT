
from math import sqrt

n=int(input())
m=int(sqrt(n))+1
a=[True]*m
a[0]=a[1]=False
end=int(sqrt(m-1))
for i in range(2,end+1):
    if a[i]:
        for j in range(i*i,m,i):
            a[j]=False
b=[i for i in range(m) if a[i]]
ans=0
for i in b:
    if i**8<=n:
        ans+=1
    else:
        break
for i in range(len(b)-1):
    if b[i]**2<=n:
        for j in range(i+1,len(b)):
            if (b[i]**2)*(b[j]**2)<=n:
                ans+=1
            else:
                break
    else:
        break
print(ans)