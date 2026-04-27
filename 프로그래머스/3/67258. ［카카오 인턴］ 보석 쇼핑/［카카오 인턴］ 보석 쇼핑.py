from collections import deque

def solution(gems):
    start, end = 0, len(gems)
    gems_len = len(set(gems))
    gems_cnt = {}

    # 일단 dict에 채우고, 맨 앞부터 구매가능한 줄 찾기
    for i in range(len(gems)):
        if gems[i] not in gems_cnt:
            gems_cnt[gems[i]] = 0
        gems_cnt[gems[i]] += 1

        if len(gems_cnt) == gems_len:
            start, end = 0, i
            break

    answer = [start + 1, end + 1]
    min_len = end - start

    queue = deque(gems[start:end + 1])

    # 앞을 줄여보고 뒤를 늘려가면서 큐 움직이기
    for i in range(end + 1, len(gems)):
        
        while queue and gems_cnt[queue[0]] > 1:
            left = queue.popleft()
            gems_cnt[left] -= 1
            start += 1

        if end - start < min_len:
            min_len = end - start
            answer = [start + 1, end + 1]

        queue.append(gems[i])
        end = i

        if gems[i] not in gems_cnt:
            gems_cnt[gems[i]] = 0
        gems_cnt[gems[i]] += 1

    while queue and gems_cnt[queue[0]] > 1:
        left = queue.popleft()
        gems_cnt[left] -= 1
        start += 1

    if end - start < min_len:
        answer = [start + 1, end + 1]
        
    return answer
