a=[]
cnt=0
n=int(input())
while n>0:
    a.append(n%10)
    n//=10
if a.count('2')>=len(a)/2:
    print("yes")
print(len(a)/2)