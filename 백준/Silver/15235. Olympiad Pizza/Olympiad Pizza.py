# 백준 15235 Olympiad Pizza

from collections import deque

n = int(input())
pizzas = list(map(int, input().split()))

queue = deque()
for i in range(n):
    queue.append((i, pizzas[i]))

answer = [0] * n
time = 0

while queue:
    idx, pieces = queue.popleft()
    time += 1
    pieces -= 1

    if pieces == 0:
        answer[idx] = time
    else:
        queue.append((idx, pieces))

print(*answer)
