from itertools import combinations

def solution(board):
    winning_cond = {
        ((0,0),(0,1),(0,2)), # 가로
        ((1,0),(1,1),(1,2)),
        ((2,0),(2,1),(2,2)),
        ((0,0),(1,0),(2,0)), # 세로
        ((0,1),(1,1),(2,1)),
        ((0,2),(1,2),(2,2)),
        ((0,0),(1,1),(2,2)), # 대각선
        ((0,2),(1,1),(2,0))
    }
    
    check_o = []
    check_x = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                check_o.append((i, j))
            elif board[i][j] == 'X':
                check_x.append((i, j))
            else:
                continue
                
    print(check_o)
    print(check_x)
    
    if len(check_o) < len(check_x) or abs(len(check_o) - len(check_x)) > 1:
        return 0

    o_win = any(all(pos in check_o for pos in cond) for cond in winning_cond)
    x_win = any(all(pos in check_x for pos in cond) for cond in winning_cond)

    if o_win and x_win:   # 둘이 동시에 이김
        return 0
    elif o_win and len(check_o) <= len(check_x):
        return 0
    elif x_win and len(check_o) > len(check_x):
        return 0
    else:
        return 1
                