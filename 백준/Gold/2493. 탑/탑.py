# 스택  |  난이도: 중
# 2493 탑

# def tower(n, ttt):
#     store = deque()
#     for i in range(n, 0, -1): # n번째 탑부터 1번 탑까지 탐색
#         count = 0
#         while ttt[i-1] >= ttt[i-1-count]: # i는 탑의 번호이므로, 인덱스로 접근할때는 i-1로 접근
#             if i-1-count == 0: # 0번 index를 넘어서 탐색하면 반복문 벗어나기
#                 break
#             count += 1
#         if ttt[i-1] < ttt[i-1-count]:
#             store.appendleft(i-count)
#         else:
#              store.appendleft(0)
        
#     return print(' '.join(map(str, store)))



import sys       
  
input = sys.stdin.readline        
N = int(input())
towers = list(map(int, input().strip().split()))
stack = [] # (index, height)
answer = []

for i in range(N):
    while stack and stack[-1][1] < towers[i]: # stack이 0이 아니고 stack마지막 요소가 지금 비교하려는 탑보다 작으면 지워버림
        stack.pop()
    if not stack: # stack 비어있으면 답에 0
        answer.append(0)
    else: # 답에 stack 마지막 요소 저장
        answer.append(stack[-1][0])
    stack.append((i + 1, towers[i])) # 현재 위치와 크기 저장
sys.stdout.write(' '.join(map(str, answer)))    
    