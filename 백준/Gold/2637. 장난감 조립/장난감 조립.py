# 위상 정렬  |  난이도: 중
# 2637 장난감 조립

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

# 기본 부품 개수 저장용: count[i][j] = i번 부품을 만들기 위해 j번 기초 부품이 몇 개 필요한가
count = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    x, y, k = map(int, input().split())
    graph[y].append((x, k))  # y → x (y가 x를 만드는데 필요함)
    indegree[x] += 1

queue = deque()

# 기초 부품(=들어오는 간선이 0인 부품) 먼저 넣기
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

        # 기초 부품은 자기 자신만 1개 필요
        count[i][i] = 1

while queue:
    now = queue.popleft()
    for next_node, weight in graph[now]:
        for i in range(1, N + 1):
            count[next_node][i] += count[now][i] * weight
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            queue.append(next_node)

# 출력: N번 부품을 만들기 위해 필요한 기초 부품만 출력
for i in range(1, N + 1):
    if count[N][i] > 0:
        print(i, count[N][i])
