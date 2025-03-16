# 수학  |  난이도: 하 
# 9020 골드바흐의 추측

T = int(input())

def makeprime(n):
    primes = list(range(n+1))
    primes[0]= primes[1] = 0
    # primes 리스트를 직접 순회하면, 중간에 리스트 값이 변경될 때 오류가 발생할 수 있어서 range(2, n+1)로 순회하는 게 안전하긴 함
    # for i in range(2, int(n**0.5) + 1):
    #     if primes[i]:
    #         for j in range(i * 2, n + 1, i):
    #             primes[j] = False
    # return primes
    for i in primes: 
        if i == 0:
            continue
        for j in range(i*2, len(primes), i):
            primes[j] = 0
    return primes

for i in range(T):
    n = int(input())
    mylist = makeprime(n)
    pos1 = pos2 = n // 2
    
    while True:
        #모두 0이 아닌 제대로 된 값이 들어갔을 때만 break문 실행
        if mylist[pos1] and mylist[pos2] and (pos1+pos2==n):
            break
        if mylist[pos1] == 0:
            pos1 -= 1
            continue
        if mylist[pos2] == 0:
            pos2 += 1
            continue
        if mylist[pos1] + mylist[pos2] < n:
            pos2 += 1
        else:
            pos1 -= 1
      
    print(f'{pos1} {pos2}')