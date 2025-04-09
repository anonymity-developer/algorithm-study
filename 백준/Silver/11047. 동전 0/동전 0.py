# 그리디  |  난이도: 하
# 11047 동전 0

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
cnt = 0

for i in range(N-1,-1,-1):
    if coins[i] <= K :
        cnt += K // coins[i]
        K %= coins[i]

print(cnt)
