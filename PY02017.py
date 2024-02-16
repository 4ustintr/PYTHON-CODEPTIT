from collections import Counter
t=int(input())
while t>0:
    t-=1
    n=int(input())
    a=list(map(int,input().split()))
    k=Counter(a)
    for i, cnt in k.items():
        if int(cnt)%2!=0:
            print(i)
    print()