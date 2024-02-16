t=int(input())
while t>0:
    t-=1
    n=input()
    a=[]
    str1=""
    s=0
    for i in range(len(n)):
        if n[i].isdigit():
             s+=int(n[i])
        if n[i].isalpha():
             a.append(n[i])
    a.sort()
    for i in range(len(a)):
         str1+=a[i]
    print(str1,s,sep="")  