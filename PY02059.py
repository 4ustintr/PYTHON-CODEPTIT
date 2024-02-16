import math
def nguyen_to(a):
    if(a<2): return False
    for i in range(2,int(math.sqrt(a))+1,1):
        if a%i==0: return False
    return True
n,m = [int(x) for x in input().split()]
a = []
maxN = 0
kq = 0
for i in range(n):
    a.append(input())
    c =[ int(x) for x in a[i].split()]
    for j in c:
        if nguyen_to(j) and j>maxN:
            maxN = j
            kq = 1
if kq ==0: print("NOT FOUND")
else:
    print(maxN)
    for i in range(n):
        c = [ int(x) for x in a[i].split()]
        for j in range(m):
            if c[j]==maxN:
                print("Vi tri [{}][{}]".format(i,j))