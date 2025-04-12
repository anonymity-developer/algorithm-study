# 1379 강의실 2
# 시작 시간 기준 오름차순 정렬
# 우선순위 큐(min-heap): (종료 시간, 강의실 번호) 저장
# → 현재 강의보다 먼저 끝나는 강의실이 있으면 재사용
# → 없으면 새 강의실 사용
# 각 강의에 할당된 강의실 번호 저장

import sys
import heapq

input = sys.stdin.readline

N = int(input())
lectures = []

for _ in range(N):
    num, start, end = map(int, input().split())
    lectures.append((start, end, num))

# 시작 시간 기준 정렬
lectures.sort()

# 현재 사용 중인 강의실 (끝나는 시간, 강의실 번호)
using_rooms = []
available_rooms = []  # 재사용 가능한 강의실 번호
room_count = 0

# 고유번호 → 강의실 번호 매핑
room_assignments = dict()

for start, end, num in lectures:
    # 끝난 강의실은 반납
    while using_rooms and using_rooms[0][0] <= start:
        _, room = heapq.heappop(using_rooms)
        heapq.heappush(available_rooms, room)

    if available_rooms:
        room = heapq.heappop(available_rooms)
    else:
        room_count += 1
        room = room_count

    heapq.heappush(using_rooms, (end, room))
    room_assignments[num] = room

# 출력
print(room_count)
for num in sorted(room_assignments):  # 고유번호 기준 정렬
    print(room_assignments[num])


