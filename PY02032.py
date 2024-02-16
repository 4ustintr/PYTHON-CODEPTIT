s=input()
str1=""
i=0
a=[]
while i<=len(s)-1:
    if len(s)%2==0:
       str1+=s[i]+s[i+1]
       a.append(str1)
       str1=""
       i+=2
    else: 
        str1+=s[i]+s[i+1]
        a.append(str1)
        str1=""
        i+=2
        if i==len(s)-1:
            break
a=set(a)
k=list(a)
k.sort()
for i in k:
  print(i,end=" ")