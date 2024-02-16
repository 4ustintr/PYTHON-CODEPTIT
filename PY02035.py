from collections import Counter
s=input()
m=int(input())
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
a.sort()
k=Counter(a)
d=0
for i,cnt in k.items():
   if int(cnt)>=m:
       print(i," ",cnt,sep=" ")
       d+=1
if d==0:
    print('NOT FOUND')