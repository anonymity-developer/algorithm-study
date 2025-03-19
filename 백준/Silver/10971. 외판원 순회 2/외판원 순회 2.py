# 완전탐색  |  난이도: 중
# 10971 외판원 순회 2


def make_min_cost(n, nbyn_list, now_visit, min_cost):
        
    if len(now_visit) == n:
        if nbyn_list[now_visit[-1]][now_visit[0]] != 0:
            now_cost = (sum(nbyn_list[now_visit[_]][now_visit[_+1]] for _ in range(n-1))) + (nbyn_list[now_visit[-1]][now_visit[0]])
            return min(min_cost, now_cost)
        return min_cost
    
    for i in range(n):
        if i not in now_visit and nbyn_list[now_visit[-1]][i] != 0:
            now_visit.append(i)
            min_cost = make_min_cost(n, nbyn_list, now_visit, min_cost)
            del now_visit[-1]
            
    return min_cost
        
  
N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
print(make_min_cost(N, W, [0], float('inf')))