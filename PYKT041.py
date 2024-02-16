from math import *


if __name__ == "__main__":
    n = int( input() )
    a = []
    for i in range( n ):
        x = input()
        a.append( x )
    hang = [0] * n
    cot = [ 0 ] * n 
    for i in range( n ):
        for j in range( n ):
            if( a[ i ][ j ] == "C" ):
                hang[ i ] += 1 
                cot[ j ] += 1
    cnt = 0 
    for i in range( n ):
        cnt += comb( hang[ i ] , 2 )
        cnt += comb( cot[ i ] , 2 )
    print( cnt )