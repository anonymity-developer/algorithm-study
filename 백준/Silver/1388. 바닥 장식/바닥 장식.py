# 1388 바닥 장식

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().strip().split())
house = [list(input().strip()) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

def bfs(x, y, symbol):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    if symbol == '-':
        dx, dy = [0, 0], [1, -1]
    else:
        dx, dy = [1, -1], [0, 0]

    while queue:
        cx, cy = queue.popleft()
        for i in range(2):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and house[nx][ny] == symbol:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

count = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            bfs(i, j, house[i][j])
            count += 1

print(count)
