# 그래프 탐색 기본  |  난이도: 하
# 1197 최소 스패닝 트리

# 크루스칼 방식

import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a_root = find(a)
    b_root = find(b)
    if a_root == b_root:
        return False
    parent[b_root] = a_root
    return True

V, E = map(int, input().split())
edges = []
for _ in range(E):
    line = input()
    if not line:
        continue  # EOF나 공백 방지
    a, b, cost = map(int, line.strip().split())
    edges.append((a, b, cost))

edges.sort(key=lambda x: x[2])
parent = [i for i in range(V + 1)]

total = 0
for a, b, cost in edges:
    if union(a, b):
        total += cost

print(total)