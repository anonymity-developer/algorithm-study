# 9095 1,2,3 더하기

def count_ways(n, total):
    if total > n:  
        return 0  # 목표 초과 → 해당 경로는 불가능하므로 0 반환
    if total == n:  
        return 1  #목표 도달 → 경우의 수 1 증가

    # 가능한 모든 경우의 수를 합산하여 반환 (재귀적으로 누적)
    return (count_ways(n, total + 1) + 
            count_ways(n, total + 2) + 
            count_ways(n, total + 3))
        

for _ in range(int(input())):
    print(count_ways(int(input()), 0)) 