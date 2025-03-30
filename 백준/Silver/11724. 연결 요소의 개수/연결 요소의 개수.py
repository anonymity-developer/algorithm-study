# 그래프 탐색 기본  |  난이도: 하
# 11724 연결 요소의 개수

from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph):
    visited = set()
    queue = deque()
    cnt = 0
    for node in graph:
        if node not in visited:
            visited.add(node)
            queue.append(node)
            while queue:
                v = queue.popleft()
                for neighbor in graph[v]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            cnt += 1
    return cnt

N, M = map(int, input().split())
graph = {i : [] for i in range(1, N+1)}

for i in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

print(bfs(graph))