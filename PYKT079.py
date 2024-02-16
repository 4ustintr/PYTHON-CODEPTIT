t=int(input())
while t>0:
    t-=1
    n=input()
    a=list(map(int,input().split()))
    a.sort()
    cnt=0
    for i in range(min(a),max(a)+1):
            if i not in a:
                  cnt+=1
    print(cnt)