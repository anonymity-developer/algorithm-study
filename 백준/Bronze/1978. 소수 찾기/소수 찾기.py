# 수학  |  난이도: 하 
# 1978 소수 찾기

# 에라토스테네스의 체

N = int(input())
M = list(map(int, input().split()))
primes = list(range(max(M) + 1))
count = 0

for i in primes:
    if i == 0:
        continue
    elif i == 1:
        primes[i] = 0
    else:
        # 지금은 index = 해당 index의 값이라서 이 접근이 가능한데 헷갈리고 별로임
        # for j in primes[i:]:
            # if j == 0:
            #     continue
            # if (j % i == 0) and (j // i >= 2):
            #     primes[j] = 0
        # i의 배수부터 i씩 늘려가면서 len(primes)까지 검사하는 구조가 효율적
        for j in range (i * 2, len(primes), i):
            primes[j] = 0

# filtered_primes = list(filter(lambda num: num != 0, primes))
# for _ in range(N):
#     if M[_] in filtered_primes:
#         count += 1    
for i in M:
    if i in primes:
        count += 1

print(count)

# 다른 사람 코드
# input()
# l=list(map(int,input().split()))
# if 1 in l: l.remove(1)
# for i in l[::]:
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0: l.remove(i);break
# print(len(l))
