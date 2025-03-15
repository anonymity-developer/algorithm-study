# 기초 (문자열)  |  난이도: 하
# 2908 상수

A, B = input().split()
print(A[::-1] if int(A[::-1]) > int(B[::-1]) else B[::-1])

# 더 간결한 코드 -> input 받을 때 바로 역순서로 슬라이싱
# print(max(input()[::-1].split(), key=int))