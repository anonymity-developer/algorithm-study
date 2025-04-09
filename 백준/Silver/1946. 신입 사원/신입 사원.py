# 그리디 | 난이도: 중
# 1946 신입사원

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    people = []
    cnt = 0

    for _ in range(int(input())):
        people.append(tuple(map(int, input().split())))

    # 서류 성적 순으로 오름차순 정렬
    people.sort(key=lambda x: x[0])
    min_interview = float('inf')

    # 면접 성적이 앞사람보다 좋을 경우에만 선발
    for _, interview in people:
        if interview < min_interview:
            cnt += 1
            min_interview = interview

    print(cnt)
