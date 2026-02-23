# 백준 13975번 파일 합치기 3

import heapq

T = int(input())

def min_value(num, num_list):
    answer = 0
    heapq.heapify(num_list)
    while len(num_list) >= 2:
        a = heapq.heappop(num_list)
        b = heapq.heappop(num_list)
        answer += (a+b)
        heapq.heappush(num_list, (a+b))
        if len(num_list) == 1:
            break
    return answer

for i in range(T):
    n = int(input())
    n_l = list(map(int, input().split()))
    print(min_value(n, n_l))
