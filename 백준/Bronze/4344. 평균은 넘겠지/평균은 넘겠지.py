# 다루는 주제: 기초(배열)  |  난이도: 하
# 4344 평균은 넘겠지

C = int(input())

for i in range(C):
    N, *M = map(int, input().split())
    sum_score = sum(M)
    highpeople = 0
    for _ in M:
        if _ > sum_score/len(M):
            highpeople += 1
    print(f"{highpeople/N*100:.3f}%")
            
            
# N, *M = map(int, input().split()) -> (*변수명)은 나머지 값을 모두 리스트로 받겠다는 뜻, Unpacking이라고 함함
# round를 써서 f-string안에 넣었을 때 40.000%를 40%로 프린트하는 출력 형식 오류 생김. f"{value.3f}" 사용하여 고정된 형식으로 출력
    
# 더 직관적인 코드
# for i in range(int(input())):
#     data = list(map(int, input().split()))  # 첫 번째 값이 학생 수, 나머지는 점수 리스트
#     N, scores = data[0], data[1:]  # 학생 수(N)와 점수 리스트(scores) 분리
#     avg_score = sum(scores) / N  # 평균 점수 계산
#     highpeople = sum(1 for score in scores if score > avg_score)  # 평균 초과 학생 수 계산
#     print(f"{highpeople / N * 100:.3f}%")  # 비율 출력 (소수점 3자리)

    