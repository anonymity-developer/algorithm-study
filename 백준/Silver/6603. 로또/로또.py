from itertools import combinations

while True:
    temp = list(map(int, input().split()))
    if len(temp) == 1:
        break
    
    k = temp[0]
    result = list(combinations(temp[1:k+1], 6))
    for i in range(len(result)):
        print(' '.join(map(str, result[i])))
    print()