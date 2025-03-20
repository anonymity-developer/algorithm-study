# 1182 부분수열의 합

def Csum(num, sequence, goal_sum, index, current_sum, cnt):
    if index == num: # 발견하면 cnt+1, 아니면 cnt 반환
        return cnt+1 if current_sum == goal_sum else cnt
    
    cnt = Csum(num, sequence, goal_sum, index + 1, current_sum + sequence[index], cnt) # 현재 원소 포함
    cnt = Csum(num, sequence, goal_sum, index + 1, current_sum, cnt) # 현재 원소 미포함
    return cnt
   
N, S = map(int, input().split())
A = list(map(int, input().split()))
print(Csum(N, A, S, 0, 0, 0) - (1 if S==0 else 0)) # 공집합을 고려한 계산