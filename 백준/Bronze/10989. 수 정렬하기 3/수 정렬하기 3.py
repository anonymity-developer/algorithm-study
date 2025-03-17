# 정렬  |  난이도: 중
# 10989 수 정렬하기 3

import sys
count = [0]*10001

for i in range(1, (int(sys.stdin.readline()))+1):
    count[int(sys.stdin.readline())] += 1
    
for j in range(1, 10001):
    if count[j] == 0:
        continue
    for _ in range(count[j]):
        print(j)