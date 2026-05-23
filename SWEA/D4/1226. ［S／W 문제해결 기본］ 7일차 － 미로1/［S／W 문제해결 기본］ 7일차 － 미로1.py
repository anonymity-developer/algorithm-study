from collections import deque


def bfs(maze, visit, start, end):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    queue = deque()
    queue.append(start)

    visit[start[0]][start[1]] = 1

    while queue:
        now_x, now_y = queue.popleft()
        if now_x == end[0] and now_y == end[1]:
            return 1

        for i in range(4):
            ax = now_x + dx[i]
            ay = now_y + dy[i]
            if 0<=ax<16 and 0<=ay<16 and maze[ax][ay]!=1 and visit[ax][ay] == 0:
                visit[ax][ay] = 1
                queue.append([ax, ay])

    return 0



for test_case in range(10):
    tc = int(input())
    answer = 0
    maze = []
    visit = [[0]*16 for _ in range(16)]
    start = [0, 0]
    end = [0, 0]
    for j in range(16):
        temp = list(map(int, input().strip()))
        if 2 in temp:
            start[0], start[1] = j, temp.index(2)
        if 3 in temp:
            end[0], end[1] = j, temp.index(3)
        maze.append(temp)
    answer = bfs(maze, visit, start, end)

    print(f'#{tc} {answer}')