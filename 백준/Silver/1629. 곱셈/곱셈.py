# 분할 정복  |  난이도: 중
# 1629 곱셈

# (a * b) mod c = ((a mod c)*(b mod c))mod c

def big_mod (a, b, c):
    if b == 0:
        return 1
    
    if b % 2 == 0:
        return (big_mod(a, b//2, c) ** 2) % c
    else:
        return (a * big_mod(a, b-1, c)) % c

A, B, C = map(int, input().split())
print(big_mod(A, B, C))