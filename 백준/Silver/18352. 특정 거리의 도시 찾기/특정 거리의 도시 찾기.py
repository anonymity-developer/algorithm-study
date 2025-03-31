# BFS  |  난이도: 하
# 18352 특정 거리의 도시 찾기

# BFS로 풀기

import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, start, length):
    
    visited = set()
    distance = [-1] * (N+1)
    distance[start] = 0
    queue = deque([start])
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                distance[neighbor] = distance[node] + 1
        
    answer = []
    for i in range(1, N+1): 
        if  distance[i] == length :
            answer.append(i)
    if len(answer) == 0:
        return print(-1)
    answer.sort()
    return print('\n'.join(map(str, answer)))

N, M, K, X = map(int, input().strip().split())
graph = {i : [] for i in range(1, N+1)}
for i in range(M):
    node1, node2 = map(int, input().strip().split())
    graph[node1].append(node2)

bfs(graph, X, K)



# 다익스트라 알고리즘으로 풀기

# import heapq

# def dijkstra(vertex, graph, length, start):
#     distance = [float('inf')] * (vertex + 1)
#     distance[start] = 0
#     pq = [(0, start)] # 비용, 노드
    
#     while pq:
#         dist, now = heapq.heappop(pq)
#         if dist > distance[now]:
#             continue
#         for neighbor, cost in graph[now]:
#             new_dist = dist + 1
#             if new_dist < distance[neighbor]:
#                 distance[neighbor] = new_dist
#                 heapq.heappush(pq, (new_dist, neighbor))
#     result = []
#     for i in range(1, vertex + 1):
#         if distance[i] == length:
#             result.append(i)
#     if not result:
#         print(-1)
#     result.sort()
#     return print('\n'.join(map(str, result)))

# N, M, K, X = map(int, input().strip().split())
# graph = {i : [] for i in range(1, N+1)}
# for i in range(M):
#     node1, node2 = map(int, input().strip().split())
#     graph[node1].append((node2, 1))

# dijkstra(N, graph, K, X)