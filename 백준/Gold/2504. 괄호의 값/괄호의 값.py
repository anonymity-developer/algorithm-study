import sys

def calc(PS):
    stack = []
    for i in PS:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            temp = 0
            while stack:
                top = stack.pop()
                if top == '(':
                    stack.append(2 if temp == 0 else 2 * temp)
                    break
                elif isinstance(top, int):
                    temp += top
                else:
                    return 0
            else:
                return 0  # ❗괄호 짝 못 찾고 끝남
        elif i == ']':
            temp = 0
            while stack:
                top = stack.pop()
                if top == '[':
                    stack.append(3 if temp == 0 else 3 * temp)
                    break
                elif isinstance(top, int):
                    temp += top
                else:
                    return 0
            else:
                return 0  # ❗괄호 짝 못 찾고 끝남
        else:
            return 0
    for s in stack:
        if not isinstance(s, int):
            return 0
    return sum(stack)

print(calc(sys.stdin.readline().strip()))
