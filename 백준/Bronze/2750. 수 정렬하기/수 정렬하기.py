# 정렬  |  난이도: 하
# 2750 수 정렬하기

import sys
input = sys.stdin.readline
print = sys.stdout.write
def q_sort(numbers, first, last):
    pl = first
    pr = last
    pivot = numbers[(pl+pr)//2]
    while pl <= pr :
        while numbers[pl] < pivot : pl += 1
        while numbers[pr] > pivot : pr -= 1
        if pl <= pr :
            numbers[pl], numbers[pr] = numbers[pr], numbers[pl]
            pl += 1
            pr -= 1
    if first < pr : q_sort(numbers, first, pr)
    if pl < last : q_sort(numbers, pl, last)
    return numbers
 
a = []   
for i in range(int(input())):
    a.append(int(input()))
q_sort(a, 0, (len(a)-1))
[print(f"{num}\n") for num in a]