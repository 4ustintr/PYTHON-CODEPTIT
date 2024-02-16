n=input()
dlow=0
dup=0
for i in n:
    if i.islower():
        dlow+=1
    if i.isupper():
        dup+=1
if dlow>=dup:
    print(n.lower())
if dup>dlow:
    print(n.upper())