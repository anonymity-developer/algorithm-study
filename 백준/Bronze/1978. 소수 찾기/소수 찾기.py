# 1978 소수 찾기

# 에라토스테네스의 체

N = int(input())
M = list(map(int, input().split()))
primes = list(range(1001))
count = 0

for i in primes:
    if i == 0:
        continue
    elif i == 1:
        primes[i] = 0
    else:
        for _ in primes[i:]:
            if _ == 0:
                continue
            if (_ % i == 0) and (_ // i >= 2):
                primes[_] = 0  # 지금 index랑 들어간 숫자랑 똑같아서 이렇게 써도 될 듯?

filtered_primes = list(filter(lambda num: num != 0, primes))

# max 사용해서 M의 최댓값을 넘어가는 primes를 검사할 필요가 없게 추가
for j in range(N):
    if M[j] in filtered_primes:
        count += 1

print(count)