# 정렬  |  난이도: 하
# 1074 Z

def Z(N, r, c, count=0):
    if N == 0:
        return count
    
    a = 2**(N-1)
    if r<a:
        if c<a : 
            count+=0
            return Z(N-1, r, c, count)
        else:
            count+=a*a
            return Z(N-1, r, c-a, count)
    else:
        if c<a : 
            count+=a*a*2
            return Z(N-1, r-a, c, count)
        else:
            count+=a*a*3
            return Z(N-1, r-a, c-a, count)
        
N, r, c = map(int, input().split())
print(Z(N, r, c))