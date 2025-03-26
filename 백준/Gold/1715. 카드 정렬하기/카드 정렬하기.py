# 스택  |  난이도: 상 
# 1715 카드 정렬하기

import heapq
import sys

input = sys.stdin.readline

heap = []
cnt = 0
for i in range(int(input().strip())):
    heapq.heappush(heap, int(input().strip()))
while len(heap) > 1:
    A = heapq.heappop(heap)
    B = heapq.heappop(heap)
    cnt += (A+B)
    heapq.heappush(heap, A+B)
    
print(cnt)
