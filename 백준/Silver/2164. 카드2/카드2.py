# 큐  |  난이도: 하
# 2164 카드2

from collections import deque

queue = deque(list(range(1, int(input())+1)))

while len(queue) > 1:
    queue.popleft()
    queue.append(queue[0])
    queue.popleft()

print(queue.pop())