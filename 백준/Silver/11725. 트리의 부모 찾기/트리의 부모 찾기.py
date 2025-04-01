# DFS  |  난이도: 중
# 11725 트리의 부모 찾기

N = int(input())
graph = {i : [] for i in range(1, 1+N)}
try:
    while True:
        node1, node2 = map(int, input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)
except EOFError:
    pass

# 반복문 버전
def dfs(graph, start):
    parent = [0] * (len(graph)+1)
    visit = set()
    stack = list()
    stack.append(start)
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.add(node)
            for neighbor in graph[node]:
                if neighbor not in visit:
                    parent[neighbor] = node
                    stack.append(neighbor)
    return parent
answer = dfs(graph, 1)
for i in answer[2:]:
    print(i)
    
# 재귀버전
# parent = [0] * (N + 1)
# def dfs(node, par):
#     for neighbor in graph[node]:
#         if neighbor != par:
#             parent[neighbor] = node
#             dfs(neighbor, node)
# dfs(1, 0)
# for i in range(2, N + 1):
#     print(parent[i])