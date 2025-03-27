# 1966 프린터 큐

from collections import deque
import sys

input = sys.stdin.readline

for i in range(int(input())):
    N, M = map(int, input().strip().split())
    M_idx = M
    sequence = list(map(int, input().strip().split()))
    sequence_queue = deque(sequence)
    cnt = 0
    while True:
        if sequence_queue[0] == max(sequence_queue):
            cnt += 1
            sequence_queue.popleft()
            if M_idx == 0:
                print(cnt)
                break
        else:
            sequence_queue.append(sequence_queue.popleft())
        M_idx -= 1
        if M_idx < 0: M_idx = len(sequence_queue) -1
        