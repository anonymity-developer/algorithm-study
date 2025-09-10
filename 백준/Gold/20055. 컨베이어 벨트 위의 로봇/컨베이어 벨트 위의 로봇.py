# 백준 20055번 컨베이어 벨트 위의 로봇

from collections import deque

n, k = map(int, input().split())
belt = deque(map(int, input().split()))
robot = deque([0] * n)
result = 0

while True:
    result += 1
    # 벨트 회전
    belt.rotate(1)
    robot[-1] = 0
    robot.rotate(1)
    robot[-1] = 0    # 내리는 위치에 도달한 경우, 즉시 내림
    # 로봇 이동
    for i in range(n - 2, -1, -1):
        if belt[i + 1] >= 1 and robot[i + 1] == 0 and robot[i] == 1:
            robot[i + 1] = 1
            robot[i] = 0
            belt[i + 1] -= 1
    robot[-1] = 0
    # 올리는 위치에 내구도 0 아니면 로봇 올리기 & 내구도 감소
    if belt[0] != 0 and robot[0] != 1:
        robot[0] = 1
        belt[0] -= 1
    # 내구도 0인 칸 수가 k이상이면 종료
    if belt.count(0) >= k:
        break
print(result)