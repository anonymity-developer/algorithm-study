# 이분 탐색  |  난이도: 중
# 2110 공유기 설치

# Parametric Search로, 나무자르기와 비슷하지만 조건 체크 함수만 다름
import sys
input = sys.stdin.readline

# 간격이 mid일 때 공유기 몇 개 설치 되는지 확인
# 처음 집 설치 후, "그 다음 집까지의 간격 >= (이전 설치 위치 + mid)" 이어야 설치가 된다
# 헷갈리면 안되는 부분 : mid는 간격이고, low와 high는 위치의 값이다
def binary_search_recursive(house_positions, house_num, WIFI_num, low, high):
    if low > high:
        return high
    mid = (low + high) // 2
    count = 1
    last_installed = house_positions[0]
    for i in range(1, house_num):
        if house_positions[i] - last_installed >= mid:
            count += 1
            last_installed = house_positions[i]
    if count >= WIFI_num:
        return binary_search_recursive(house_positions, house_num, WIFI_num, mid + 1, high)
    else:
        return binary_search_recursive(house_positions, house_num, WIFI_num, low, mid - 1)

N, C = map(int, input().split())
WIFI = [int(input()) for _ in range(N)]
WIFI.sort()
print(binary_search_recursive(WIFI, N, C, 1, WIFI[-1] - WIFI[0]))