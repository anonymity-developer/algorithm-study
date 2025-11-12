# 백준 1644번 소수의 연속합

N = int(input())
answer = 0

# 예외 처리: 2 미만이면 만들 수 있는 연속 소수 합 없음
if N < 2:
    print(0)
    exit()

# 에라토스테네스의 체 (i*i부터 지우기)
temp_list = [i for i in range(N + 1)]
temp_list[0] = 0
temp_list[1] = 0

limit = int(N ** 0.5)
for i in range(2, limit + 1):
    if temp_list[i] != 0:
        start = i * i
        step = i
        for m in range(start, N + 1, step):
            temp_list[m] = 0

prime_list = [v for v in temp_list if v > 0]

# 두 포인터로 연속합 세기 (오른쪽 늘리고, N 이상이면 왼쪽 줄이기)
left = 0
right = 0
temp_sum = 0

while True:
    if temp_sum >= N:
        if temp_sum == N:
            answer += 1
        temp_sum -= prime_list[left]
        left += 1
    else:
        if right == len(prime_list):
            break
        temp_sum += prime_list[right]
        right += 1

print(answer)
