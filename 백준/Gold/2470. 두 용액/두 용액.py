# 이분탐색  |  난이도: 중 
# 2470 두 용액

# 이분 탐색 써서 시간 초과 난 코드

# import sys
# input = sys.stdin.readline

# def test(num, nums): # 음수를 하나 받고, 양수 리스트에서 음수와 더했을 때 절댓값이 가장 작아지는 것을 찾음
#     first = 0
#     last = len(nums)- 1
#     value = float("inf")
#     mid_store = float("inf")
#     while first <= last:
#         mid = (first + last) // 2
#         if num + nums[mid] == 0: # 음수 + 양수가 0이면, 바로 리턴
#             value = 0
#             return [num, nums[mid], value]
#         elif num + nums[mid] > 0: # 음수 + 양수가 양수면, 좀 더 작은 양수값 검사
#             if value > abs(num + nums[mid]):
#                 value = abs(num + nums[mid])
#                 mid_store = nums[mid]
#             last = mid - 1
#         else: # 음수 + 양수가 음수면, 좀 더 작은 양수값 검사
#             if value > abs(num + nums[mid]):
#                 value = abs(num + nums[mid]) 
#                 mid_store = nums[mid]
#             first = mid + 1
#     return num, mid_store, value

# def solutions(Alist, Blist):
#     if len(Alist) == 0:
#         return Blist[-2], Blist[-1]
#     if len(Blist) == 0:
#         return Alist[0], Alist[1]
#     store = [0, 0, float("inf")]
#     for i in Alist:
#         temporary = test(i, Blist)
#         store = temporary if store[2] > temporary[2] else store
#         if store[2] == 0:
#             break
#     return print(f'{store[0]} {store[1]}')

# A, B = [], []
# for _ in range(int(input())):
#     nums = list(map(int, input().split()))
#     A.extend([x for x in nums if x < 0])
#     B.extend([x for x in nums if x > 0])
# solutions(A, B)


# 투 포인터 쓰는게 정석 ^.^

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()  # 반드시 정렬!

left = 0
right = N - 1
min_abs_sum = float('inf')
best_pair = (arr[left], arr[right])

while left < right:
    current_sum = arr[left] + arr[right]
    if abs(current_sum) < min_abs_sum:
        min_abs_sum = abs(current_sum)
        best_pair = (arr[left], arr[right])
        if min_abs_sum == 0:  # 0이면 더 이상 확인할 필요 없음
            break
    if current_sum < 0:
        left += 1  # 합이 음수 → 더 큰 수가 필요함
    else:
        right -= 1  # 합이 양수 → 더 작은 수가 필요함

print(f"{best_pair[0]} {best_pair[1]}")