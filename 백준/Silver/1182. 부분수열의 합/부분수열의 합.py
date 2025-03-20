def Csum(num, sequence, goal_sum, index, current_sum, cnt):
    if index == num:
        return cnt+1 if current_sum == goal_sum else cnt
    
    cnt = Csum(num, sequence, goal_sum, index + 1, current_sum + sequence[index], cnt)
    cnt = Csum(num, sequence, goal_sum, index + 1, current_sum, cnt)
    return cnt
   
   
N, S = map(int, input().split()) 
print(Csum(N, list(map(int, input().split())), S, 0, 0, 0) - (1 if S==0 else 0))