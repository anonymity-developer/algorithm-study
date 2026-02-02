# 백준 2615번 오목

import sys

input = sys.stdin.readline
gomoku = []
for i in range(19): #0~18
    gomoku.append(list(map(int, input().split())))
winner = 0
location = [0, 0]

def check_win(r, c):
    BW = gomoku[r][c]

    # 세로
    if (r+4) < 19:
        if r-1 >= 0 and gomoku[r-1][c] == BW:
            pass
        else:
            for i in range(1, 5):
                if BW != gomoku[r+i][c]:
                    break
                if i == 4:
                    if r+5 < 19 and gomoku[r+5][c] == BW:
                        break
                    return True

    # 가로
    if (c+4) < 19:
        if c-1 >= 0 and gomoku[r][c-1] == BW:
            pass
        else:
            for i in range(1, 5):
                if BW != gomoku[r][c+i]:
                    break
                if i == 4:
                    # 6목 체크(오른쪽 1칸 더)
                    if c+5 < 19 and gomoku[r][c+5] == BW:
                        break
                    return True

    # 대각선 ↘
    if (r+4) < 19 and (c+4) < 19:
        if r-1 >= 0 and c-1 >= 0 and gomoku[r-1][c-1] == BW:
            pass
        else:
            for i in range(1, 5):
                if BW != gomoku[r+i][c+i]:
                    break
                if i == 4:
                    if r+5 < 19 and c+5 < 19 and gomoku[r+5][c+5] == BW:
                        break
                    return True

    # 대각선 ↗
    if (r-4) >= 0 and (c+4) < 19:
        if r+1 < 19 and c-1 >= 0 and gomoku[r+1][c-1] == BW:
            pass
        else:
            for i in range(1, 5):
                if BW != gomoku[r-i][c+i]:
                    break
                if i == 4:
                    if r-5 >= 0 and c+5 < 19 and gomoku[r-5][c+5] == BW:
                        break
                    return True

    return False

found = False
for i in range(19):
    for j in range(19):
        if gomoku[i][j]:
            if check_win(i, j):
                winner = gomoku[i][j]
                location[0], location[1] = i+1, j+1
                found = True
                break
    if found:
        break

print(winner)
if winner:
    print(*location)
