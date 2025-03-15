# 기초 (배열)  |  난이도: 하 
# 2577 숫자의 개수

A, B, C = [int(input()) for _ in range(3)] # list comprehension 사용
multiplication = str(A*B*C)
numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(numbers)):
    numbers[i] = multiplication.count(str(i))
for _ in range(len(numbers)):
    print(numbers[_])
    
# list comprehension과 join()을 이용하여 더 간단히 만들기 가능
# numbers = [multiplication.count(str(i)) for i in range(10)] 
# print("\n".join(map(str, numbers)))