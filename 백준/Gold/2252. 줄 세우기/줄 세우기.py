# 위상 정렬  |  난이도: 하
# 2252 줄 세우기
 
from collections import deque

N, M = map(int, input().split())
graph = {i : [] for i in range(N+1)}
for i in range(M):
    node1, node2  = map(int, input().split())
    graph[node1].append(node2)

def topology_sort(n, graph):
    indegree =[0] * (n+1)
    for u in range(n+1):
        for v in graph[u]:
            indegree[v] += 1
    
    queue = deque([i for i in range(1, n+1) if indegree[i] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)        
    return result

print(' '.join(str(_) for _ in topology_sort(N, graph)))