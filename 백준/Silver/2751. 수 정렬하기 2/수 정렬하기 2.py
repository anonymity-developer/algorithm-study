# 정렬  |  난이도: 중
# 2751 수 정렬하기 2

import sys

A = []
for i in range(int(sys.stdin.readline())):
    A.append(int(sys.stdin.readline()))
A.sort()
[sys.stdout.write(f'{i}\n') for i in A]