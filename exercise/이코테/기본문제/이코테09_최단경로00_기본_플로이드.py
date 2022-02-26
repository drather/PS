"""
플로이드 워셜 알고리즘
1. 인접행렬 형태의 그래프를 INF 로 초기화한다.
2. 대각 원소를 0으로 초기화한다.
3. 간선들을 읽어, 그 가중치값을 그래프에 업데이트한다.

4. (핵심) i, j, k 세 인덱스를 통해서, graph 에 최단거리 값을 업데이트한다.
    - i: 행 번호
    - j: 열 번호
    - graph[i][j]: i 에서 j 까지 가는 최단 경로
    - graph[i][k] + graph[k][j]: i 에서 k 를 거쳐 j 까지 가는 경로

"""

node_num = int(input())
link_num = int(input())

INF = int(1e9)

graph = [[INF] * (node_num+1) for _ in range(node_num+1)]

for i in range(1, node_num+1):
    graph[i][i] = 0

for _ in range(link_num):
    src, trg, wgt = map(int, input().split())
    graph[src][trg] = wgt

for g in graph:
    print(g)

for i in range(1, node_num + 1):
    for j in range(1, node_num + 1):
        for k in range(1, node_num + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


for i in range(1, node_num + 1):
    print(graph[i][1:])
