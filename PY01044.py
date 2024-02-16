'''
s1=list(input().split())
s2=list(input().split())
n=""
a=[]
for i in s1:
    if i not in s2:
        n+=i
        n+=" "
for i in s2:
    n+=i
    n+=" "
for i in n:
    print(i,end=" ")
a.sort()
print(n)
'''
if __name__ == "__main__":
  s1 = set(input().lower().split(' '))
  s2 = set(input().lower().split(' '))
  for x in sorted(s1.union(s2)):
    print(x, end = ' ')
  print()
  for x in sorted(s1.intersection(s2)):
    print(x, end = ' ')
  print()



