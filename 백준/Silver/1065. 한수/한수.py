# 수학  |  난이도: 하 
# 1065 한수

def hansu(str_n):
    count = 0
    if len(str_n) < 3:
        count = int(str_n)
    else:
        count += 99
        # 1000 예외처리 해줘야하는데 999랑 답이 같고 받는 값이 1=<n=<1000이라 지금은 안해줘도 ㄱㅊ
        for i in range(100, int(str_n)+1):
            a = str(i) # 문자열끼리 그냥 덧셈해버리면 계산되는 게 아니라 연결되버리는 것 유의
            if int(a[0])+int(a[2])==2*int(a[1]) or int(a[0])==int(a[1])==int(a[2]):
                count += 1
    return count

print(hansu(input()))

# 훨씬 좋은 코드 -> map(int, str(i)) 사용하면 바로 a, b, c 만들기 가능, a-b == b-c 연산
# def hansu(n):
#     n = int(n)
#     if n < 100:
#         return n
#     count = 99
#     for i in range(100, n + 1):
#         a, b, c = map(int, str(i))
#         if a - b == b - c:
#             count += 1    
#     return count

# GPT 코드
# def hansu(n):
#     n = int(n)  
#     return n if n < 100 else 99 + sum(1 for i in range(100, n + 1) if (i // 100 - (i // 10) % 10) == ((i // 10) % 10 - i % 10))
