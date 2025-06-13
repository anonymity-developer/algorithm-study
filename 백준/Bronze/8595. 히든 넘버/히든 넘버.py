# 백준 8595 히든 넘버

n = int(input())
A = input()

temp = ""
result = 0

for i in A:
    if i.isdigit(): # 숫자면 문자로 저장해둠
        temp += i
    else: # 문자면 지금까지 쌓인 temp를 숫자로 변환해서 더함
        if temp != "":
            result += int(temp)
            temp = ""

if temp != "": # A가 숫자로 끝났을 때를 고려한 처리
    result += int(temp)

print(result)
