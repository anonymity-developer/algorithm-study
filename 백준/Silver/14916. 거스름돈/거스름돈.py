n = int(input())

cnt = 0

if n == 1 or n == 3:
    cnt = -1
else:
    cnt += n // 5
    n %= 5

    if n % 2 != 0:
        cnt -= 1
        n += 5
        cnt += n // 2
    else :
        cnt += n // 2

print(cnt)