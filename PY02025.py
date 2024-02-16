n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = list(set(a))
b = list(set(b))
a.sort()
b.sort()
giao = []
hab = []
hba = []
for i in a:
    if i in b:
        giao.append(i)
    else:
        hab.append(i)
for i in b:
    if i not in a:
        hba.append(i)
for i in giao:
    print(i, end=' ')
print()
for i in hab:
    print(i, end=' ')
print()
for i in hba:
    print(i, end=' ')