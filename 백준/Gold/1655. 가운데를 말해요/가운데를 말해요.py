# 우선순위 큐  |  난이도: 중
# 1655 가운데를 말해요

import heapq
import sys

input = sys.stdin.readline

# Maxheap = [] # 클수록 위로 가는 Maxheap(음수 씌워서 관리), 작을수록 위로 가는 Minheap
# 작은 수는 maxheap으로, 큰 수는 minheap으로
# 두 heap의 크기는 1보다 크게 차이나지 않게 관리(루트 떼어서 보내기)
# 만약 홀수개의 입력일때 minheap의 크기가 더 큰 상황이라면 루트 떼어서 maxheap으로 보내줘야 함
# maxheap의 루트가 뽑아야하는 답

# n은 1일때 처리
# 처음 두 값 중 작은 수를 maxheap으로, 큰 수를 minheap으로

def find_median(N):
    Maxheap = [] # 클수록 위로(음수 씌워서 관리)
    Minheap = [] # 작을수록 위로
    for i in range(N):
        num = int(input())
        # Maxheap 비어있거나 받은 값이 Maxheap 루트보다 작거나 같으면 → 작은 값이니까 Maxheap에 넣기
        if not Maxheap or num <= -(Maxheap[0]): 
            heapq.heappush(Maxheap, -num)
        else:
            heapq.heappush(Minheap, num)
        if len(Maxheap) > len(Minheap) + 1:
            heapq.heappush(Minheap, -heapq.heappop(Maxheap))
        elif len(Minheap) > len(Maxheap):
            heapq.heappush(Maxheap, -heapq.heappop(Minheap))
        print(-Maxheap[0])
            
N = int(input())
find_median(N)