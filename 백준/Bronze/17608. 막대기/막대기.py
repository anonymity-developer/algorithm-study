# 스택  |  난이도: 하
# 17608 막대기

import sys
input = sys.stdin.readline

N = int(input())
sticks = []
cnt = 0
now = 0

for i in range(N):
    sticks.append(int(input()))
    
for i in range(N-1, -1, -1):
    if sticks[i] > now:
        now = sticks[i]
        cnt += 1
        
print(cnt)