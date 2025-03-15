# 기초(문자열)  |  난이도: 하
# 2675 문자열 반복

# 내가 처음 작성한 코드. 문자열을 불필요하게 리스트로 받음
# T = int(input())
# for i in range(T):
#     N, *M = input().split()
#     print(''.join(M[0][i]*int(N) for i in range(len(M[0]))))

T = int(input())
for i in range(T):
    N, M = input().split()
    print(''.join(_ * int(N) for _ in M))