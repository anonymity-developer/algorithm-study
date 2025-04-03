# 2667 단지 번호 붙이기

from collections import deque

N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().strip())))
visited = [[False]*N for _ in range(N)]
nums = []

def bfs(graph, visited, start):
    
    queue = deque([start])
    visited[start[0]][start[1]] = True
    cnt = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    
    while queue:
        nowx, nowy = queue.popleft()
        for i in range(4):
            nx = nowx + dx[i]
            ny = nowy + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    cnt += 1
    return cnt   

for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j] == 1:
            nums.append(bfs(graph, visited, (i, j)))
            
nums.sort()
print(len(nums))
print('\n'.join(str(num) for num in nums))
