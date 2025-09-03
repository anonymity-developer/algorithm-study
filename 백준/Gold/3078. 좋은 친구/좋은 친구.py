#  백준 3078번 좋은 친구

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
check_list = [[] for _ in range(21)]
count = 0

for i in range(1, N+1):
    temp = input().strip()
    check_list[len(temp)].append(i)
    

for group in check_list:
    size = len(group)
    if size <= 1:
        continue
    start = 0
    for end in range(size):
        while group[end] - group[start] > K:
            start += 1
        count += end - start

print(count)