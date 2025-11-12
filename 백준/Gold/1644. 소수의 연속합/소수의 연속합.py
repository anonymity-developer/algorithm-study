# 백준 1644번 소수의 연속합

N = int(input())
answer = 0

if N < 2:
    print(answer)
    exit()

# 에라토스테네스의 체로 소수 구하기
temp_list = [i for i in range(N+1)]
temp_list[1] = 0
for i in range(2, N//2 + 1):
    if temp_list[i] != 0:
        multiple_cnt = 2
        while temp_list[i] * multiple_cnt <= N:
            temp_list[i * multiple_cnt] = 0
            multiple_cnt += 1
prime_list = list(filter(lambda n : n > 0, temp_list))

# 밀어가면서 더해보기
for j in range(len(prime_list)):
    temp_sum = 0
    idx_cnt = 0
    while j + idx_cnt < len(prime_list):
        temp_sum += prime_list[j + idx_cnt]
        if temp_sum >= N:
            if temp_sum == N:
                answer += 1
            break
        idx_cnt += 1
        
print(answer)