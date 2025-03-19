# 완전탐색  |  난이도: 하 
# 2309 일곱 난쟁이

height = []
for _ in range(9):
    height.append(int(input()))
sum_height = sum(height)

for i in range(8):
    for j in range(i+1, 9):
        if sum_height - height[i] - height[j] == 100:
            del height[j]
            del height[i]
            height.sort()
            print('\n'.join(map(str, height)))
            break
    if len(height) == 7: break
    
# sys.exit는 코드 진행 자체가 완전 종료되므로, 일반적으로 braek나 flag를 사용
