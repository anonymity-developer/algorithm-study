from itertools import permutations
import math

def dfs(sp, cnt, weak, dist):
    # sp: 현재 커버해야 할 weak의 인덱스
    # cnt: 지금까지 사용한 친구 수 (== 다음에 쓸 친구의 인덱스)
    
    # 모든 weak 커버 완료
    if sp >= len(weak):
        return cnt
    
    # 친구를 다 썼는데 weak가 남은 경우
    if cnt >= len(dist):
        return math.inf
    
    # 이번에 투입할 친구가 커버할 수 있는 끝 위치
    limit = weak[sp] + dist[cnt]
    
    # 이번 친구로 커버 가능한 마지막 weak 인덱스(next_sp) 찾기
    next_sp = sp
    while next_sp < len(weak) and weak[next_sp] <= limit:
        next_sp += 1
    
    # 다음 친구(cnt+1)로 남은 weak(next_sp부터) 커버하러 DFS
    return dfs(next_sp, cnt + 1, weak, dist)


def solution(n, weak, dist):
    check_count = len(weak)
    # 원형을 일자로 펴기 위해 weak를 두 번 이어붙임
    extended_weak = weak + [w + n for w in weak]
    
    min_friends = math.inf
    
    # 시작 위치를 weak의 각 지점으로 모두 시도
    for start_idx in range(check_count):
        # start_idx 기준으로 길이 check_count만큼의 구간을 하나의 "직선"으로 보고 풀기
        line_weak = extended_weak[start_idx:start_idx + check_count]
        
        # 친구 투입 순서를 전부 DFS로 탐색
        for order in permutations(dist, len(dist)):
            use_cnt = dfs(0, 0, line_weak, order)
            min_friends = min(min_friends, use_cnt)
    
    # 해답이 없으면 -1
    return -1 if min_friends == math.inf else min_friends
