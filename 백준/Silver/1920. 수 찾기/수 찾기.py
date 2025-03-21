import sys
import bisect

N = int(input())
card = list(map(int, input().split()))
card.sort()
M = int(input())
target = list(map(int, input().split()))


def binary_search(ordered_list, _target):
    index = bisect.bisect_left(ordered_list, _target)

    if index < len(ordered_list) and ordered_list[index] == _target:
        return index
    else:
        return None


for i in target:
    result = binary_search(card, i)

    if result is None:
        print('0')
    else:
        print('1')