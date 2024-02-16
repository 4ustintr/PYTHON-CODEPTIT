if __name__ == '__main__':
    n = int(input())
    while n>0:
        n-=1
        s1 = input()
        s2 = input()
        tmp1 = sorted(s1)
        tmp2 = sorted(s2)
        print(f'Test {i}:', end = ' ')
        if tmp1 == tmp2:
            print('YES')
        else:
            print('NO')