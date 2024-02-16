
n,m =[int(x) for x in input().split()]
a = []
minN = int(1e6)
maxN = -int(1e6)
for i in range(n):
    a.append(input())
for i in range(n):
    minN = min(minN,min(int(x) for x in a[i].split()) )
    maxN = max(maxN,max(int(x) for x in a[i].split()) )
kq = 1
for i in range(n):
    c = [int(x) for x in a[i].split()]
    for j in range(len(c)):
        if int(c[j]) == (maxN-minN):
            if kq==1:
                print(maxN-minN)
            print("Vi tri [{}][{}]".format(i,j))
            kq = 0
if kq == 1:
    print("NOT FOUND")

        