n=int(input())
while n>0:
    s=input()
    a=[int(i) for i in str(s)]
    for i in range(len(a)-1,0,-1):
        if a[i]>=5:
            a[i-1]+=1
        a[i]=0
    print(''.join([str(i) for i in a]))
    n-=1