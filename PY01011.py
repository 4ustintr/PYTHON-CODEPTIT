n=int(input())
def kt(s):
    if len(s)%2==1 or s!= s[::-1]:
        return False
    for i in s:
       if int(i)%2==1:
           return False
    return True
while n>0:
    a=int(input())
    for i in range(22,a,2):
        if kt(str(i)):
            print(i,end=" ")
    n-=1
    print()
