# 백준 11643 소인수 분해

# N = int(input())
# make = [True]*(N+1)
# make[0], make[1] = 0, 0
# primes = [] # 에라토스테네스의 체로 소수 구하기기
# for i in range(2, N+1): 
#     if make[i]:
#         primes.append(i)
#         for j in range(2*i, N+1, i):
#             make[j] = False

# for num in primes:
#     if num > N : # N이 더 안나눠지면 break
#         break
#     while True:
#         if N % num == 0:
#             print(num)
#             N //= num
#         else:
#             break
    
N = int(input())

i = 2
while i * i <= N:
    while N % i == 0:
        print(i)
        N //= i
    i += 1

if N > 1:
    print(N)
    