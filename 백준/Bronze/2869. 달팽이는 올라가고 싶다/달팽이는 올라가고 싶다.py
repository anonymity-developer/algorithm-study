# 수학  |  난이도: 하
# 2869 달팽이는 올라가고 싶다

# while 써서 구현한 거 시간 초과 걸려서 다시 풀기

A, B, V = map(int, input().split())
print((V-B-1)//(A-B)+1)