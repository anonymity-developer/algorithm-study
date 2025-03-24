# 큐  |  난이도: 하
# 11866 요세푸스 문제 0

from collections import deque

def Josephus(N, K):
    noname = deque(range(1, N+1))
    sequence = []
    
    while len(noname) != 0:
        for _ in range(K-1):
            noname.append(noname[0])
            noname.popleft()
        sequence.append(noname[0])
        noname.popleft()
    
    return print(f"<{', '.join(map(str, sequence))}>")

N, K = map(int, input().split())
Josephus(N, K)