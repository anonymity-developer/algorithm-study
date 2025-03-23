# 스택  |  난이도: 하
# 9012 괄호

for i in range(int(input())):
    PS = list(input())
    VPS = []
    for j in range(len(PS)):
        if PS[j] == '(':
            VPS.append('+')
        if PS[j] == ')':
            if len(VPS) == 0:
                VPS.append('-')
                break
            else:
                VPS.pop()
    print('YES') if (len(VPS) == 0) else print('NO')