t=int(input())
while t>0:
    t-=1
    s = input()
    a = []
    cnt = 1
    for i in s:
        if i == '(':
            a.append(cnt)
            print(cnt, end = ' ')
            cnt += 1
        elif i == ')':
            print(a.pop(), end = ' ')
    print()