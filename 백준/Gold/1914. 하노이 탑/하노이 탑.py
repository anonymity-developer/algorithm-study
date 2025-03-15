# 재귀함수  |  난이도: 하
# 1914 하노이 탑

# 최소 이동 횟수 점화식은 H(n)=2H(n−1)+1
# 점화식을 풀면 지수적인 증가, H(n)=2**n-1

# 재귀 호출하면서 기둥의 역할이 바뀜 (source → auxiliary, auxiliary → destination 순환)
# 1: (n-1개) S to A // 2 : (큰거 1개) S to D // 3 : (n-1개) A to D

def hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f'{source} {destination}')
    else : 
        hanoi(n-1, source, destination, auxiliary)
        print(f'{source} {destination}')
        hanoi(n-1, auxiliary, source, destination)

n = int(input()) 
print(2**n-1)
if n <= 20:
    hanoi(n, 1, 2, 3)