# 그래프 탐색 기본  |  난이도: 하
# 5639 이진 검색 트리

# node 없는, 인덱스 범위 기반 재귀 분할

import sys
sys.setrecursionlimit(10**6)

preorder = []
while True:
    line = sys.stdin.readline()
    if not line:
        break
    preorder.append(int(line.strip()))

def postorder(start, end):
    if start > end:
        return
    
    root = preorder[start]
    idx = end + 1

    for i in range(start + 1, end + 1):
        if preorder[i] > root:
            idx = i
            break

    postorder(start + 1, idx - 1)
    postorder(idx, end)
    print(root)

postorder(0, len(preorder) - 1)



# node로 BST를 재구성하는 방식

# import sys
# sys.setrecursionlimit(10**6)

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

# def insert(node, val):
#     if val < node.val:
#         if node.left is None:
#             node.left = Node(val)
#         else:
#             insert(node.left, val)
#     else:
#         if node.right is None:
#             node.right = Node(val)
#         else:
#             insert(node.right, val)

# def postorder(node):
#     if node is None:
#         return
#     postorder(node.left)
#     postorder(node.right)
#     print(node.val)

# preorder = []
# while True:
#     try:
#         line = sys.stdin.readline()
#         if not line:
#             break
#         preorder.append(int(line.strip()))
#     except:
#         break

# root = Node(preorder[0])
# for val in preorder[1:]:
#     insert(root, val)

# postorder(root)
