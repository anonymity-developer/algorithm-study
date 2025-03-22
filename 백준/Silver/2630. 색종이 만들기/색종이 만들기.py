# 분할 정복  |  난이도: 하
# 2630 색종이 만들기

import sys

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

blue = 0
white = 0

def cutting(x, y, size):
    global white, blue
    now = paper[x][y]
    
    for i in range(x, x+size):
        for j in range(y, y+size):
            if paper[i][j] != now:
                new_size = size // 2
                cutting(x, y, new_size)
                cutting(x, y + new_size, new_size)
                cutting(x + new_size, y, new_size)
                cutting(x + new_size, y + new_size, new_size)
                return
    if now == 0:
        white += 1
    else:
        blue += 1
    
cutting(0, 0, N)
print(f'{white}\n{blue}')