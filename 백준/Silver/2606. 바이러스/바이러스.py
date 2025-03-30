# 그래프 탐색 기본  |  난이도: 하
# 2606 바이러스

from collections import deque

vertex = int(input())
edge = int(input())
visited = [False] * (vertex+1)
graph = {i : [] for i in range(1, vertex+1)}
for i in range(edge):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        now = queue.popleft()
        for neighbor in graph[now]:
            if visited[neighbor] == False:
                visited[neighbor] = True
                queue.append(neighbor)
    return (sum(visited)-1)

print(bfs(graph, 1, visited))
    