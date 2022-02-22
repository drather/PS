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
