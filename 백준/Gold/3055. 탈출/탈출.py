# BFS  |  난이도: 중
# 3055 탈출

from collections import deque

R, C = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(input()))
    
water = []
safe = set()
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'D':
            dest = (i, j)
        elif graph[i][j] == 'S':
            start = (i, j)
        elif graph[i][j] == 'X':
            safe.add((i, j))
        elif graph[i][j] == '*':
            water.append((i, j))
    
def 고슴도치(graph, start, dest):
    www = deque(water)
    kkk = deque([start])
    visited = [[False]*C for _ in range(R)]
    visited[start[0]][start[1]] = True
    day = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while kkk:
        day += 1
        for _ in range(len(www)):
            x, y = www.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < R and 0 <= ny < C:
                    if graph[nx][ny] == '.':
                        graph[nx][ny] = '*'
                        www.append((nx, ny))
        for _ in range(len(kkk)):
            x, y = kkk.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < R and 0 <= ny < C:
                    if not visited[nx][ny] and (graph[nx][ny] == '.' or graph[nx][ny] == 'D'):
                        if (nx, ny) == dest:
                            return day
                        visited[nx][ny] = True
                        kkk.append((nx, ny))
    return "KAKTUS"

print(고슴도치(graph, start, dest))

    