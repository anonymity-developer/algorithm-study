T = int(input())

for i in range(T):
    # result = []
    # result.append(input().split('X')) -> split('X')가 이미 리스트를 반환하기 때문에 이중 리스트 생겨버림림
    result = input().split('X')
    score = 0
    for i in range(len(result)):
        score += sum(range(1, len(result[i])+1))
    print(score)