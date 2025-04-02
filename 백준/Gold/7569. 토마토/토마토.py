# BFS  |  난이도: 중
# 7569 토마토

# 다중 시작점 BFS

from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().strip().split())
box = [[list(map(int, input().strip().split())) for i in range(N)] for j in range(H)]
                
def bfs(three_d):
    dz = [-1, 1, 0, 0, 0, 0]
    dx = [0, 0, -1, 1, 0, 0]
    dy = [0, 0, 0, 0, -1, 1]
    queue = deque()
    all_tomato = 0 # 전체 토마토 수 
    ripe_tomato = 0 # 익은 토마토 수
    day = 0 # 큐가 빌 때까지(더 이상 익을 애가 없을 때까지지) 카운트
    
    for z in range(H):
        for x in range(N):
            for y in range(M):
                if three_d[z][x][y] == 1:
                    queue.append((z, x, y))
                    ripe_tomato += 1
                if three_d[z][x][y] != -1:
                    all_tomato += 1
                    
    while queue:
        for _ in range(len(queue)): # 큐에 지금 들어있는 애들만큼 (익은 지 하루 된 애들)
            z, x, y = queue.popleft()
            for i in range(6):
                nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
                if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M:
                    if three_d[nz][nx][ny] == 0:
                        three_d[nz][nx][ny] = 1
                        queue.append((nz, nx, ny))
                        ripe_tomato += 1
        if queue:
            day += 1
        
    return day if ripe_tomato == all_tomato else -1

print(bfs(box))