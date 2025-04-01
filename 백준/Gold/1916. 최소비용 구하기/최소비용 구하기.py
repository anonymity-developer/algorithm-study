# BFS  |  난이도: 중
# 1916 최소 비용 구하기

import heapq

def dijkstra(graph, start, dest):
    n = len(graph)
    distance = [float('inf')] * (n+1)
    distance[start] = 0
    pq = [(0, start)]  # (비용, 노드)

    while pq:
        dist, now = heapq.heappop(pq)
        if now == dest:
            break
        if dist > distance[now]:
            continue
        for neighbor, cost in graph[now]:
            new_dist = dist + cost
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return print(distance[dest])

N = int(input())
M = int(input())
graph = {i : [] for i in range(1, N+1)}
for i in range(M):
    s, d, w = map(int, input().split())
    graph[s].append((d, w))
start, dest = map(int, input().split())

dijkstra(graph, start, dest)
    