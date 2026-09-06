n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
ans = 0

for i in range(n - 2):
    for j in range(n - 2):
        Sum = sum(
            matrix[i + x][j + y]
            for x in range(3)
            for y in range(3)
        )
        ans = max(ans, Sum)
print(ans)