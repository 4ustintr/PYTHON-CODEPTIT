n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a=set(a)
b=set(b)
cnt=0
for x in a:
    if x in b:
        cnt+=1
if len(a)==len(b) and cnt==len(a):
    print("YES")
else:
    print('NO')
