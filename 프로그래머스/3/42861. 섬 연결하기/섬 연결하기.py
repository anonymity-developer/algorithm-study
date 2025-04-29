def solution(n, costs):
    # 1. 간선 비용 기준 정렬
    costs.sort(key=lambda x: x[2])

    # 2. 부모 테이블 초기화
    parent = [i for i in range(n)]

    # 3. find 함수 (부모 찾기)
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # 경로 압축
        return parent[x]

    # 4. union 함수 (합치기)
    def union(x, y):
        x_root = find(x)
        y_root = find(y)
        if x_root != y_root:
            parent[y_root] = x_root  # x의 부모로 y를 합침
            return True
        return False

    answer = 0

    # 5. 크루스칼 본격 실행
    for a, b, cost in costs:
        if union(a, b):  # 연결이 가능하면
            answer += cost

    return answer
