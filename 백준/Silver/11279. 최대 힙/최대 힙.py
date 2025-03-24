# 우선순위 큐 |  난이도: 하
# 11279 최대 힙

import heapq
import sys

answer = []
heap = []

for i in range(int(sys.stdin.readline().strip())):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        if heap:
            answer.append(-(heapq.heappop(heap)))
        else:
            answer.append(0)
    else:
        heapq.heappush(heap, -(num))
        
sys.stdout.write('\n'.join(map(str, answer)))