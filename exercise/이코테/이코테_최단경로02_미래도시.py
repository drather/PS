city_num, link_num = map(int, input().split())

INF = int(1e9)

graph = [[INF] * (city_num+1) for _ in range(city_num+1)]

for _ in range(link_num):
    src, trg = map(int, input().split())
    graph[src][trg] = 1
    graph[trg][src] = 1

for i in range(1, city_num+1):
    graph[i][i] = 0

for k in range(1, city_num+1):
    for i in range(1, city_num+1):
        for j in range(1, city_num+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

destination1, destination2 = map(int, input().split())

for i in range(1, city_num+1):
    for j in range(1, city_num+1):
        print(graph[i][j], end=' ')
    print()


answer = graph[1][destination1] + graph[destination1][destination2]

if answer >= INF:
    print(-1)
else:
    print(answer)
