# 수학  |  난이도: 하 
# 1978 소수 찾기

# 에라토스테네스의 체 방식 활용용. 소수만 있는 리스트를 만들고 받은 리스트와 비교해서 값이 있으면 카운트 하는 식
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
        # (기존) 리스트의 값 자체를 순회하며 배수를 제거하려고 했지만, primes[i:]가 변경될 때 문제가 발생 가능 -> 돌아가긴 함
        # for j in primes[i:]:
            # if j == 0:
            #     continue
            # if (j % i == 0) and (j // i >= 2):
            #     primes[j] = 0
        # (수정) i의 배수부터 i씩 증가하면서 리스트 길이까지 반복하는 구조가 정확하고 효율적
        for j in range (i * 2, len(primes), i):
            primes[j] = 0

# (기존) 필터링해서 따로 저장하고 다시 비교하는 방식 : 메모리 낭비
# filtered_primes = list(filter(lambda num: num != 0, primes))
# for _ in range(N):
#     if M[_] in filtered_primes:
#         count += 1    
# (수정) 필터링 없이 바로 `primes`에서 0이 아닌 값과 비교
for i in M:
    if i in primes:
        count += 1

print(count)

# 다른 사람 코드 -> 받은 숫자들에 대해서만 j(2부터 i**0.5+1)로 나눠떨어지는지 검사
# 검사중인 숫자(i)가 j(2부터 i**0.5+1)로 나눠 떨어지는게 있으면 리스트에서 i값을 지우고 break해서 다음 숫자(i+1)값 검사
# 에라토스테네스의 체 방식이 아니라 받은 수들을 하나하나 계산해서 소수 아닌 애들 remove 해버리는 식
# j가 i 자신(j == i)이 되는 경우는 없으므로 소수는 지워지지 않음
# input()
# l=list(map(int,input().split()))
# if 1 in l: l.remove(1)
# for i in l[::]:
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0: l.remove(i);break
# print(len(l))
