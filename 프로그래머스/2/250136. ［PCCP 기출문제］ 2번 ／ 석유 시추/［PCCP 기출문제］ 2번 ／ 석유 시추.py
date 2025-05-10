from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    col_result = [0] * m

    visited = [[False] * m for _ in range(n)]  # 🔧 고친 부분: visited를 바깥에서 한 번만 생성

    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True  # 🔧 고친 부분: 방문 체크는 큐에 넣을 때 해야 함

                count = 1
                columns = set()
                columns.add(j)

                while queue:
                    x, y = queue.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < n and 0 <= ny < m:
                            if land[nx][ny] == 1 and not visited[nx][ny]:
                                visited[nx][ny] = True 
                                queue.append((nx, ny))
                                count += 1
                                columns.add(ny)  # 🔧 고친 부분: 해당 열 집합 기록

                for c in columns:
                    col_result[c] += count  # 해당 열이 포함된 덩어리의 전체 크기를 누적

    return max(col_result)
