import sys
input = sys.stdin.readline

R, C, N = map(int, input().split())
bombs = [list(input().strip()) for _ in range(R)]
check = [[-1]*C for _ in range(R)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 초기 폭탄
for i in range(R):
    for j in range(C):
        if bombs[i][j] == 'O':
            check[i][j] = 3

time = 1
while time < N:
    time += 1

    if time % 2 == 0:
        # 폭탄 설치
        for i in range(R):
            for j in range(C):
                if bombs[i][j] == '.':
                    bombs[i][j] = 'O'
                    check[i][j] = time + 3
    else:
        # 폭탄 폭발
        to_explode = []
        for i in range(R):
            for j in range(C):
                if check[i][j] == time:
                    to_explode.append((i, j))

        for x, y in to_explode:
            bombs[x][y] = '.'
            check[x][y] = -1
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < R and 0 <= ny < C:
                    if bombs[nx][ny] == 'O' and check[nx][ny] != time:
                        bombs[nx][ny] = '.'
                        check[nx][ny] = -1

for row in bombs:
    print(''.join(row))