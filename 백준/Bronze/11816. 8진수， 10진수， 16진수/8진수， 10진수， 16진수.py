# 백준 11816 8진수, 10진수, 16진수

X = input()

if X[0] == '0' and X[1] == 'x': # 16진수면
    result = 0        
    match = {"a":10, "b":11, "c":12, "d":13, "e":14, "f":15}
    for i in range(2, len(X)):
        if X[i] in match:
            temp = match[X[i]]
        else:
            temp = int(X[i])
        result += (temp)*(16**(len(X)-(i+1)))
    print(result)
        
elif X[0] == '0': # 8진수면
    result = 0
    for i in range(1, len(X)):
        result += int(X[i])*(8**(len(X)-(i+1)))
    print(result)
        
else: # 10진수면
    print(X)