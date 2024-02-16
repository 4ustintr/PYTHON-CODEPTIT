n=int(input())
while n>0:
    s=input()
    for i in range(len(s)):
        if s[i].isdigit():
            for j in range(int(s[i])-1):
                print(s[i-1],end="")
        else:
            print(s[i],end="")
    n-=1
    print()