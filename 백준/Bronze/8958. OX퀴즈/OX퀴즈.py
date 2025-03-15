# 기초(배열)  |  난이도: 하
# OX퀴즈

T = int(input())

for i in range(T):
    # result = []
    # result.append(input().split('X')) -> split('X')가 이미 리스트를 반환하기 때문에 이중 리스트 생겨버림
    result = input().split('X')
    score = 0
    for i in range(len(result)):
        score += sum(range(1, len(result[i])+1))
    print(score)
    
# GPT 형님 코드
# 입력받는 문자열 자체로 바로 반복문을 돌릴 수 있다
# for _ in range(int(input())):
#     score = consecutive = 0
#     for i in input():
#         consecutive = consecutive + 1 if ch == 'O' else 0
#         score += consecutive
#     print(score)

# generator expression을 이용 가능 : sum(1 for _ in "banana" if ch == 'a') 하면 a 개수만큼 더해짐
# sum(expression for variable in iterable if condition)
