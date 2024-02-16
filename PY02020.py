n=int(input())
a=list(map(float,input().split()))
k=[]
for i in range(len(a)):
    if a[i]!=max(a) or a[i]!=min(a):
        k.append(a[i])
print('{:.2f}'.format(sum(res) / len(res)))