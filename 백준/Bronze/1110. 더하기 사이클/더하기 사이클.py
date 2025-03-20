#  1110 더하기 사이클

N = int(input())
count = 0
now = 0 # now는 계속 str으로 남아있게 하기

if N < 10:
    now = str(0)+str(N)
    now = str(now[-1]) + (str(int(now[0])+int(now[-1])))[-1] # str(뒤) + str(앞+뒤 합의 뒤쪽 수) => now로 업데이트
    count += 1
else: 
    now = str(N)
    now = now[-1] + (str(int(now[0])+int(now[-1])))[-1]
    count += 1
while N != int(now):
    now = str(now)
    now = now[-1] + (str(int(now[0])+int(now[-1])))[-1]
    count += 1
    
print(count)