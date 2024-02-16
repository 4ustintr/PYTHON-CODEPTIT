import math
def check(n):
    k=int(n)
    if k<2:
        return False
    else:
        if k==2 and k==3:
            return True
        for i in range(2,int(math.sqrt(k))+1):
            if k%i==0:
                return False
        return True
if __name__=="__main__":
    t=int(input())
    while t>0:
        t-=1
        n=int(input())
        b=[]
        for i in range(n):
            k=str(i)
            d=k[::-1]
            if check(k) and check(d) and k!=d and int(d)<n :
                if k not in b:
                    b.append(i)
                    b.append(d)
        for i in b:
          print(i,end=" ")
        print()
