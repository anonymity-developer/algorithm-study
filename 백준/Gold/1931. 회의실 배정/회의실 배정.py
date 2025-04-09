# 그리디  |  난이도: 중
# 1931 회의실 배정

N = int(input())
meetings =[tuple(map(int, input().split())) for i in range(N)]
cnt = 0

meetings.sort(key = lambda x: (x[1], x[0])) # 끝나는 시간 빠른 순서
now_f, now_l = map(int, (0, 0))

for start, end in meetings:
    if start >= now_l: # 시작 시작이 끝나는 시간보다 클 때만 예약(빨리 끝나는 순 정렬이라 다른 경우 신경 안써도 됨)
        cnt += 1
        now_l = end

print(cnt)