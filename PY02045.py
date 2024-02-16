n = input()
while len(n)>1:
    k = len(n)//2
    n = str(int(n[0:k])+int(n[k:]))
    print(n)