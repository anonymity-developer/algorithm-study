# 우선순위 큐  |  난이도: 상
# 13334 철로

# 시간초과 난 코드
# import sys
# input = sys.stdin.readline

# def findmaxpeople(Lines, D):
#     now = float('inf')
#     real_cnt = 0
#     for i in range(N):
#         if now == Lines[i][0]:
#             continue
#         now = Lines[i][0]
#         cnt = 0
#         j = 0
#         while i + j < len(Lines) and Lines[i + j][0] <= now + D:
#             if now <= Lines[i+j][0] and Lines[i+j][1] <= now + D :
#                 cnt += 1
#             j += 1
#         if real_cnt < cnt:
#             real_cnt = cnt
#     return sys.stdout.write(str(real_cnt) + '\n')
    
# lines = []
# N = int(input())
# for _ in range(N):
#     a, b = list(map(int, input().split()))
#     if a > b:
#         a, b = b, a
#     lines.append((a, b))
# lines.sort()
# d = int(input())
# findmaxpeople(lines, d)

# 힙 이용 코드
import sys
import heapq
input = sys.stdin.readline

N = int(input())
people = []
for _ in range(N):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    people.append((a, b))

d = int(input())
people.sort(key=lambda x: x[1])

heap = []
answer = 0

for a, b in people:
    start = b - d
    heapq.heappush(heap, a)
    while heap and heap[0] < start:
        heapq.heappop(heap) # 힙에 넣기 전에 범위 밖의 사람은 제거
    answer = max(answer, len(heap))

print(answer)