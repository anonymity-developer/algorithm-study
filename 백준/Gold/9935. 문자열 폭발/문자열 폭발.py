# 9935 문자열 폭발

alpha = input()
bomb = input()
result = []

for i in alpha:
    result.append(i)
    if len(result) >= len(bomb) and result[-(len(bomb)):] == list(bomb):
        for j in range(len(bomb)):
            result.pop()
print('FRULA' if not result else ''.join(result))