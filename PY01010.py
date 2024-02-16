n=int(input())
while n>0:
    a=input()
    k=list(a)
    s1=k[0]+k[1]
    s2=k[len(k)-2]+k[len(k)-1]
    if s1==s2:
        print("YES")
    else:
        print("NO")
    n-=1
