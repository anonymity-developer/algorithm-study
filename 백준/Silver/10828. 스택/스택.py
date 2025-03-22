# 스택  |  난이도: 하
# 10828 스택

import sys

class Stack:
    
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def empty(self):
        return 1 if len(self.items) == 0 else 0
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if self.empty(): #만약 empty가 true라면
            return -1
        return self.items.pop()
    
    def top(self):
        if self.empty():
            return -1
        return self.items[-1]

stack = Stack()
n = int(sys.stdin.readline())
for _ in range(n):
    cmd = sys.stdin.readline().strip().split()
    if cmd[0] == 'push':
        stack.push(int(cmd[1]))
    elif cmd[0] == 'pop':
        print(stack.pop())
    elif cmd[0] == 'size':
        print(stack.size())
    elif cmd[0] == 'empty':
        print(stack.empty())
    elif cmd[0] == 'top':
        print(stack.top())