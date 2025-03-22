# 조건 판단 함수와 이분 탐색 함수를 나누고, 반복문 기반으로 동작하는 ver.
def is_enough(trees, height, target):
    total = 0
    for tree in trees:
        if tree > height:
            total += tree - height
    return total >= target # (일정 h로 잘랐을 때 잘려나온 값들의 합) >= (목표)이면 true 반환
def binary_search(trees, target):
    low = 0
    high = max(trees)
    result = 0
    while low <= high:
        mid = (low + high) // 2
        if is_enough(trees, mid, target):
            result = mid
            low = mid + 1 # true 반환받았으면 더 높은 길이로 잘라보기
        else:
            high = mid - 1 # false 반환받았으면 더 높은 길이로 잘라보기
    return result


# 함수 하나로, 재귀 함수 이용하는 ver.
# def binary_search_recursive(trees, target, low, high):
#     if low > high:
#         return high
#     mid = (low + high) // 2
#     total = sum(tree - mid for tree in trees if tree > mid)
#     if total >= target:
#         return binary_search_recursive(trees, target, mid + 1, high)
#     else:
#         return binary_search_recursive(trees, target, low, mid - 1)


N, M = map(int, input().split())
trees = list(map(int, input().split()))
print(binary_search(trees, M))