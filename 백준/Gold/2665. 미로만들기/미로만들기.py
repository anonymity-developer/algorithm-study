# BFS  |  난이도: 중
# 2665 미로 만들기

# 가중치가 0 또는 1임
# 1) 0-1 BFS (deque 이용) -> 흰방(0)은 앞쪽에, 검은방(1)은 뒤쪽에 넣어서 우선순위 조정
# 2) 다익스트라 -> 벽을 부순 횟수를 비용으로 간주해서 최솟값 갱신

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    dist = [[float('inf')] * N for _ in range(N)]
    dist[x][y] = 0
    dq = deque()
    dq.append((x, y))
    
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                # 다음 칸이 흰방이면 비용 0
                if graph[nx][ny] == 1 and dist[nx][ny] > dist[x][y]:
                    dist[nx][ny] = dist[x][y]
                    dq.appendleft((nx, ny))  # 흰방 → 앞으로
                # 검은방이면 벽 하나 부수기 → 비용 +1
                elif graph[nx][ny] == 0 and dist[nx][ny] > dist[x][y] + 1:
                    dist[nx][ny] = dist[x][y] + 1
                    dq.append((nx, ny))      # 검은방 → 뒤로
    return dist[N-1][N-1]
    

cnt = 0
N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]
print(bfs(0, 0))
