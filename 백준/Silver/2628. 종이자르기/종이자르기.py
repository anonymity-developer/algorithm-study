# 수학  |  난이도: 하
# 2628 종이자르기

x, y = list(map(int, input().split()))
row = []
col = []
# 리스트에 한번에 여러 요소 추가 -> extend써야함. 만약 append 쓰면 [y, 0]이 하나의 요소로 들어가버림
# 원점 위치와 
# 주어지는 사각형 크기도 그냥 그걸로 잘랐다고 인식하기. x는 가장 크게 자르는 열, y는 가장 크게 자르는 행
row.extend([y, 0])
col.extend([x, 0])
for i in range(int(input())):
    temporary = list(map(int, input().split()))
    if temporary[0] == 0:
        row.append(temporary[1])
    else:
        col.append(temporary[1])
row.sort(reverse=True) # 가로로 자르는 애들 큰 순서대로 정렬 
col.sort(reverse=True) # 세로로 자르는 애들 큰 순서대로 정렬 

extents = []
# 0에서 자르려고 하지 않게 범위 설정 잘해주기
for i in range(len(row)-1):
    for j in range(len(col)-1):
        extents.append((row[i]-row[i+1])*(col[j]-col[j+1]))
print(max(extents))