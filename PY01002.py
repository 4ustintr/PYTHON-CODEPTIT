n=input()
a=list(n)
b=int(a[0])
c=int(a[4])
d=int(a[len(a)-1])
if (b+c)==d:
    print("YES")
else:
    print("NO")